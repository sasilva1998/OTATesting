from main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
   
   o = OTAUpdater('https://github.com/sasilva1998/OTATesting.git')
   o.download_and_install_update_if_available('NETLIFE-Silva', 'SASM3141')


def start():
	for i in range(0,15):
		print(i*2)


def boot():
    download_and_install_update_if_available()
    start()


boot()