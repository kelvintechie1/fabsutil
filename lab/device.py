from . import deviceobject
from . import interfaceobject
from . import linkobject

def buildSupportedDevices(allDevices, allInterfaces, allLinks, platform):
    all = []
    for deviceAndInterface in zip(allDevices, allInterfaces):
        all.append(deviceobject.Device(deviceAndInterface[0], deviceAndInterface[1],
                                       [link for link in allLinks
                                        if deviceAndInterface[0]["id"] in
                                        [link["node_a"], link["node_b"]]], platform))
        
    supported = [device for device in all if device.os is not None]

    return {"all": all, "supported": supported}