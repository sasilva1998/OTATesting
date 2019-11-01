from main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
   
   o = OTAUpdater('https://github.com/sasilva1998/OTATesting.git',main_dir='/')
   o._download_and_install_update('NETLIFE-Silva', 'SASM3141')


def start():
	for i in range(0,10):
		print(i*3)


def boot():
    download_and_install_update_if_available()
    start()


boot()
