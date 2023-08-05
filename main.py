from urllib3 import disable_warnings
disable_warnings()

from api import apicaller
from device import device

if __name__ == "__main__":
    api = apicaller.createAuthedAPISession()
    devices = device.buildSupportedDevices(api.buildDevicesList(), "cml")
