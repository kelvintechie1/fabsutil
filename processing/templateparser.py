from random import randint
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from errors import inputerrors
from re import findall
from processing import custom_j2filters

class TemplateParser:
    def __init__(self):
        self.path = (Path(__file__).parents[1] / "data" / "user").resolve()
        self.env = Environment(
            loader=FileSystemLoader(self.path), 
            autoescape=True,
            undefined=StrictUndefined)
        
        self.env.filters["regex"] = custom_j2filters.regexFilter

    def readTemplate(self, fileName):
        with open(self.path / fileName, "r") as file:
            lines = file.readlines()
        return (lines, self.env.get_template(fileName))

    def parseIPAddressPattern(self, fileName, dnum):
        (templateText, templateObject) = self.readTemplate(fileName)
        if len(templateText) != 1:
            raise inputerrors.InvalidTemplateException(str(fileName))

        randomVars = [randint(0, 255) for var in findall(r"\{\{ (r\[[0-9]\]) \}\}", templateText[0])]
        
        return templateObject.render(device=dnum, randnum=randomVars)

    def parseDeviceNumberPattern(self, fileName, dname):
        return self.readTemplate(fileName)[1].render(name=dname)