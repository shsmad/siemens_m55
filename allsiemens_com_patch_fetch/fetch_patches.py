from __future__ import annotations

import os
import re
from argparse import ArgumentParser

import requests

LIST_URL = "http://allsiemens.com/patch/{model}-{fw}-{page}.htm"
VIEW_URL = "http://allsiemens.com/patch/view-{patch_id}.htm"
DOWNLOAD_URL = "http://allsiemens.com/patch/view.php?download={patch_id}"
ASCII_STRIP_RE = re.compile(r"[^\w\"\+.-]")


def fetch_file(url: str, filename: str) -> str:
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as resp:
        resp.raise_for_status()
        with open(filename, "wb") as fhandle:
            for chunk in resp.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                fhandle.write(chunk)
    return filename


def get_links_for_patches(model: str = "M55", fw: str = "sw11", page: int = 1) -> list:
    url = LIST_URL.format(model=model, fw=fw, page=page)
    resp = requests.get(url).text

    patches = re.findall(
        r"/patch/view-(?P<patch_id>\d+)\.htm'>(?P<patch_title>.*?)</a>",
        resp,
        flags=re.IGNORECASE | re.DOTALL,
    )

    pages = [
        int(x)
        for x in re.findall(
            r"/patch/{model}-{fw}-(\d+).htm".format(model=model, fw=fw),
            resp,
            flags=re.IGNORECASE | re.DOTALL,
        )
    ]

    if page + 1 in pages:
        return patches + get_links_for_patches(model=model, fw=fw, page=page + 1)
    else:
        return patches


def download_patch(patch_id: int, title: str, model: str = "M55", fw: str = "sw11") -> str:
    url = VIEW_URL.format(patch_id=patch_id)
    resp = requests.get(url).text

    dep_str = re.search(
        r"Зависимости</i>: \[ (.*?) \]<br><i>Модель",
        resp,
        flags=re.IGNORECASE | re.DOTALL,
    )

    filename = f"{patch_id}-{title}"

    if dep_str:
        deps = re.findall(
            r"view-(\d+)\.htm",
            dep_str.groups()[0],
            flags=re.IGNORECASE | re.DOTALL,
        )
        filename += "--deps-" + "+".join(deps)

    for sep in os.path.sep, os.path.altsep:
        if sep:
            filename = filename.replace(sep, " ")

    filename = filename.replace("&quot;", '"')

    filename = str(ASCII_STRIP_RE.sub("", "_".join(filename.split()))).strip("._")

    os.makedirs(f"patches/{model}_{fw}/", exist_ok=True)

    return fetch_file(
        url=DOWNLOAD_URL.format(patch_id=patch_id), filename=f"patches/{model}_{fw}/{filename}.vkp"
    )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-m", "--model", dest="model", help="Модель телефона", default="M55")
    parser.add_argument("-s", "--software", dest="fw", help="Прошивка", default="sw11")
    args = parser.parse_args()

    patches = get_links_for_patches(model=args.model, fw=args.fw)
    for patch in patches:
        print(  # NOQA: T001
            download_patch(patch_id=int(patch[0]), title=patch[1], model=args.model, fw=args.fw)
        )
