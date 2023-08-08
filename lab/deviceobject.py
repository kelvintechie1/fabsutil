from json import load
from pathlib import Path
from . import portobject, interfaceobject

class Device:
    with open((Path(__file__).parents[1] / "data/deviceMappings.json").resolve(), 
              "r") as file:
        mappings = load(file)

    def __init__(self, apiOutput, ports, links, platform):
        for property in apiOutput:
            setattr(self, property, apiOutput[property])

        self.interfaces = {}

        self.findOS(platform)
        self.addPorts(ports, links)
    
    def findOS(self, platform):
        osTypeFound = False
        for os in Device.mappings[platform].items():
            try:
                os[1].index(self.nodeType)
                self.os = os[0]
                osTypeFound = True
                break
            except ValueError:
                self.os = None
                continue
    
    def addPorts(self, ports, links):        
        self.ports = {}
        filteredPorts = [port for port in ports
                              if port["connected"]]
        if len(filteredPorts) != 0:
            for port in filteredPorts:
                self.ports[port["id"]] = portobject.Port(port)
                self.ports[port["id"]].addLinks(links)
    
    def addIPInterface(self, intType, intPrefix, intNum, ipAddresses):
        self.interfaces[f"{intPrefix}{intNum}"] = interfaceobject.IPInterface(
            intType, intPrefix, intNum, ipAddresses)
    
    def __str__(self):
        output = f"{self.id}: {self.name}, {self.os}\n"
        for port in self.ports.items():
            output += ' '.join(["Port:", str(port[1]), "/ "])
            for link in port[1].links.items():
                output += ' '.join(["Link:", str(link[1])])
            output += "\n"
        output += "\n"
        return output