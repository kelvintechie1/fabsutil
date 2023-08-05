from urllib3 import disable_warnings
disable_warnings()

from api import apicaller
from lab import device
from settings.readSettings import readSettings

if __name__ == "__main__":
    settings = readSettings()
    api = apicaller.createAuthedAPISession(settings["general"]["url"], settings["general"]["trustcert"])
    devices = device.buildSupportedDevices(api.buildDevicesList(settings["platform"]["lab_id"]), settings["platform"]["appliance"])