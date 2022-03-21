Release Information

App (setup.exe) Version: V4.0.100 (06/26/2003)
App (DRemover.exe) Version: V1.3.0.1 (12/06/2002)
Driver Version for Win98 & Me: V2.0.0.0 (11/25/2002)
Driver Version for Win2K/XP: V2.0.0.8 (05/07/2003)

Files Included in This Release:
	DRemover.exe
	readme.txt
	serwpl.inf
	setup.exe
	Win98_ME\ser9pl.sys
	Win98_ME\serspl.inf
	Win98_ME\serspl.vxd
	Win2K_XP\pl2303.cat
	Win2K_XP\ser2pl.inf
	Win2K_XP\ser2pl.sys
			
Changes in this Release:
	1. For Windows2000 and XP: Bugfix regarding hardware handshake signals and other minor changes to increase 
		system stability. Passed MicroSoft Windows logo testing (WHQL).
	2. For Windows2000 and XP: Change of the driver version and date to V2.0.0.8, 05/07/2003.
	3. For Windows98 and ME: No change.
	4.'setup.exe' has been added.


	
Note:   1. The USB-DC is designed only for 500mA USB-Ports. 
	   	Operation on a 100mA port may cause undesired results including system instability and loss of data.

	2. During the installation under WindowsXP, if you assign the path manually, please assign the path to 
		"\Win2K_XP\..." Otherwise you'll get a warning message, because a required file cannot be found. 
	
	3. After installation of the USB data cable driver and plugged-in data cable, a virtual COM port will be 
		generated. The name and index of the allocated COM port can be accessed via the 'Device Manager'. 

	4. For deinstallation, after installation via 'setup.exe', please use the Control Panel - Add/Remove Program.

	5. After installation via Hardware Assistant the driver is not visible in the Control Panel. 
		Use for deinstallation the file 'DRemover.exe', stored on the driver CD.

	6. In case of any COM-port allocation conflict (e.g. with an onboard modem), 
		choose a higher COM port manually (e.g. above port 10) via 'Device Manager' for the USB data cable.

	7. Uninstall notice: If you reinstall the driver by "setup.exe" before you uninstall the driver, 
		the USB data cable must be plugged into the PC at least once. If you don't follow this recommendation, 
		an uninstall notice may occur.

	8. It is a system characteristic of USB that if you unplug the data cable after driver installation and plug it into another 
		physical USB port on the same PC or hub, the driver will be installed again.  The new installation of the 
		driver will be done automatically by the PC; no user activities are required. 
		However, the number of the COM port will change. If you have chosen a COM port manually, you will have to 
		reassign the new physical USB port.

	

For FAQ and future updates of the USB device driver please visit the web: 
www.my-siemens.com

-------------------------------------------------------------------------------------------------------


Information sur ce release

Version de l'appl. (setup.exe) : V4.0.100 (04/15/2003)
Version de l'appl. (DRemover.exe) : V1.3.0.1 (12/06/2002)
Version du pilote pour Win98 & Me : V2.0.0.0 (11/25/2003)
Version du pilote pour Win2K/XP: V2.0.0.8 (05/07/2003)

Fichiers inclus dans ce release :
	DRemover.exe
	readme.txt
	serwpl.inf
	setup.exe
	Win98_ME\ser9pl.sys
	Win98_ME\serspl.inf
	Win98_ME\serspl.vxd
	Win2K_XP\pl2303.cat
	Win2K_XP\ser2pl.inf
	Win2K_XP\ser2pl.sys
			
Changements de ce release :

	1. Pour Windows2000 et XP : Bugfix concernant les signaux d��tablissement de liaison (�handshake? 
		g�n�r�s par le mat�riel et autres changements mineurs pour augmenter la stabilit?du syst�me.
    		Test du logo MicroSoft Windows r�ussi (WHQL)
	2. Pour Windows2000 et XP : changement de la version de pilote et de la date en 
		V2.0.0.7, 01/24/2003 
	3. Pour Windows98 et Me : aucune modification
	4.'setup.exe' a �t?ajout?

	
Rem. :  1. L'USB-DC peut uniquement s'utiliser sur un port USB 500mA. 	   	
		Toute utilisation sur un port 100mA peut provoquer des effets non d�sir�s dont une instabilit?
                du syst�me et des pertes de donn�es.
	   		   
	2. Sous WindowsXP : l'installation via 'Setup.exe' n'est pas support�e. Utilisez l'Assistant Mat�riel pour 
		installer le pilote.
	
	3. Une fois l'installation du pilote du c�ble de donn�es USB r�alis�e et le c�ble de donn�es enfich? 
                un port COM virtuel est cr��. Le nom/ index du port COM attribu?est visible dans le 'Gestionnaire de p�riph�riques'. 

	4. Pour d�sinstaller un pilote install?avec 'setup.exe', utilisez le Panneau de configuration - 
                Ajout/Suppression de programmes.

	5. Apr�s une installation avec l'Assistant Mat�riel, le pilote n'appara�t pas dans le Panneau de configuration. 
                Pour le d�sinstaller, utilisez le fichier 'DRemover98_2K.exe' sur le CD de pilotes.

	6. En cas de conflit d'attribution du port COM (par exemple avec un modem int�gr?, 
		s�lectionner pour le c�ble de donn�es USB un port COM plus �lev?(par exemple sup�rieur au port 10) 
		?l'aide du "Gestionnaire de p�riph�riques".
	7. Avis de d�sinstallation : si vous r�installez le pilote avec "setup.exe" sans l'avoir pr�alablement d�sinstall? 
		le c�ble de donn�es USB doit �tre branch?sur le PC une fois au moins. 
		Si vous ne respectez pas cette recommandation, un avis de d�sinstallation sera affich?	
	8. Cette caract�ristique syst�me est propre au standard USB. Elle d�clenche la r�installation du pilote si vous 
		d�branchez le c�ble de donn�es apr�s avoir install?le pilote et que vous le rebranchez 	
		sur un autre port physique USB du m�me PC ou concentrateur. 
		La r�installation du pilote est r�alis�e automatiquement par le PC ; 
		aucune intervention de l'utilisateur n'est n�cessaire. Cependant, le num�ro du port COM changera. 
		Si vous avez choisi un port COM manuellement, vous devrez r�affecter le nouveau port physique USB.

Pour vous informer sur les questions fr�quentes (FAQ) et les futures mises ?jour du pilote du p�riph�rique USB, 
visitez le site web ?l�adresse suivante: www.my-siemens.com

	
