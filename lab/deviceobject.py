from json import load
from pathlib import Path

class Device:
    with open((Path(__file__).parent.parent / "data/deviceMappings.json").resolve(), 
              "r") as file:
        mappings = load(file)

    def __init__(self, apiOutput, platform):
        for property in apiOutput:
            setattr(self, property, apiOutput[property])
        
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
        return f"{self.id}: {self.name}, {self.os}"