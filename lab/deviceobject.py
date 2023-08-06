from json import load
from pathlib import Path
from . import interfaceobject

class Device:
    with open((Path(__file__).parent.parent / "data/deviceMappings.json").resolve(), 
              "r") as file:
        mappings = load(file)

    def __init__(self, apiOutput, interfaces, links, platform):
        for property in apiOutput:
            setattr(self, property, apiOutput[property])

        self.findOS(platform)
        self.addInterfaces(interfaces, links)
    
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
    
    def addInterfaces(self, interfaces, links):        
        self.interfaces = {}
        filteredInterfaces = [interface for interface in interfaces
                              if interface["connected"]]
        if len(filteredInterfaces) != 0:
            for interface in filteredInterfaces:
                self.interfaces[interface["id"]] = interfaceobject.Interface(interface)
                self.interfaces[interface["id"]].addLinks(links)
    
    def __str__(self):
        output = f"{self.id}: {self.name}, {self.os}\n"
        for interface in self.interfaces.items():
            output += ' '.join(["Interface:", str(interface[1]), "/ "])
            for link in interface[1].links.items():
                output += ' '.join(["Link:", str(link[1])])
            output += "\n"
        output += "\n"
        return output