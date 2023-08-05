from . import deviceobject

def buildSupportedDevices(allDevices, platform):
    all = [deviceobject.Device(labDevice, platform)
                  for labDevice in allDevices]
    supported = [device for device in all if device.os is not None]

    return {"all": all, "supported": supported}