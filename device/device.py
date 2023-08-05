from json import load
from pathlib import Path

class Device:
    with open((Path(__file__).parent.parent / "data/deviceToOSMappings.json").resolve(), 
              "r") as file:
        mappings = load(file)

    def __init__(self, apiOutput, legend, platform):
        for property in enumerate(apiOutput):
            setattr(self, legend[property[0]], property[1])
        
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
    
    def __str__(self):
        return f"{self.nodeid}: {self.name}, {self.os}"