from ota_updater import OTAUpdater


def download_and_install_update_if_available():
    ota_updater = OTAUpdater('https://github.com/sasilva1998/OTATesting')
    ota_updater.download_and_install_update_if_available('FLIA SILVA','generacionsilva1976')

def start():
  for i in range(0,5):
    print(i*2)

def boot():
    download_and_install_update_if_available()
    start()
    
boot()
