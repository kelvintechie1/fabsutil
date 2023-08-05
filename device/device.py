from . import deviceobject

def buildSupportedDevices(allDevices, platform):
    allDevices = [deviceobject.Device(labDevice, ["nodeid", "name", "nodeType"], platform) 
                  for labDevice in allDevices]
    
    return [device for device in allDevices if device.os is not None]