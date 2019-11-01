from main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
   
   o = OTAUpdater('https://github.com/sasilva1998/OTATesting.git')
   o.download_and_install_update_if_available('NETLIFE-Silva', 'SASM3141')


def start():
	from main import ota_updater
	from main.action import process

	process()
	o = OTAUpdater('https://github.com/sasilva1998/OTATesting.git')
   	o.download_and_install_update_if_available('NETLIFE-Silva', 'SASM3141')
	o.check_for_update_to_install_during_next_reboot()


def boot():
    download_and_install_update_if_available()
    start()


boot()
