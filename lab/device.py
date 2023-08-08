from . import deviceobject
from . import portobject
from . import linkobject

def buildSupportedDevices(allDevices, allPorts, allLinks, platform):
    all = []
    for deviceAndPort in zip(allDevices, allPorts):
        all.append(deviceobject.Device(deviceAndPort[0], deviceAndPort[1],
                                       [link for link in allLinks
                                        if deviceAndPort[0]["id"] in
                                        [link["node_a"], link["node_b"]]], platform))
        
    supported = [device for device in all if device.os is not None]

    return {"all": all, "supported": supported}