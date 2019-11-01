from main.ota_updater import OTAUpdater
import main.ota_updater


def download_and_install_update_if_available():
   
   o = OTAUpdater('https://github.com/sasilva1998/OTATesting.git')
   o.download_and_install_update_if_available('NETLIFE-Silva', 'SASM3141')


def start():
	import time

	for i in range(0,10):
		print(i*3)

	time.sleep(3)
	ota_updater.check_for_update_to_install_during_next_reboot()


def boot():
    download_and_install_update_if_available()
    start()


boot()
