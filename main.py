from ota_update.main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
   
   o = OTAUpdater('url-to-your-github-project')
   o.download_and_install_update_if_available('wifi-ssid', 'wifi-password')


def start():
	for i in range(0,5):
    print(i*2)


def boot():
    download_and_install_update_if_available()
    start()


boot()