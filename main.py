from urllib3 import disable_warnings
disable_warnings()

from api import apicaller
from lab import device
from settings.readSettings import readSettings

if __name__ == "__main__":
    settings = readSettings()
    api = apicaller.createAuthedAPISession(settings["general"]["url"], settings["general"]["trustcert"])
    allDevices = api.buildDevicesList(settings["platform"]["lab_id"])
    links = api.buildLinksList(settings["platform"]["lab_id"])
    interfaces = [api.buildInterfacesList(settings["platform"]["lab_id"], device["id"])
                  for device in allDevices]
    
    devices = device.buildSupportedDevices(allDevices, interfaces, links,
                                           settings["platform"]["appliance"])

    print(*devices["all"], sep="\n")