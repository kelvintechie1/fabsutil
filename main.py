from urllib3 import disable_warnings
disable_warnings()

from api.cml import cmlapi
from device import device
from getpass import getpass

if __name__ == "__main__":
    apiObject = cmlapi.API(baseURL="https://ktl-csco-cml01.lab.trankelvin.com/api/v0",
                           username=input("Enter your username: "),
                           password=getpass("Enter your password: "))
    
    if apiObject.authAPI() is not None:
        print("Authentication error. Validate your credentials/parameters and try again.")
        exit(-1)

    
    allDevices = []
    
    for labDevice in apiObject.buildDevicesList():
        allDevices.append(device.Device(labDevice, ["nodeid", "name", "nodeType"], "cml"))
    
    supportedDevices = [device for device in allDevices if device.os is not None]
    
    for supportedDevice in supportedDevices:
        print(supportedDevice)
