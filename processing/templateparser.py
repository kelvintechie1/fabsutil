from random import randint
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, meta
from errors import inputerrors
from re import findall

def parseIPAddressPattern(templateName, dnum):
    path = (Path(__file__).parents[1] / "data" / "user").resolve()
    with open(fileName := (path / "routerid.j2"), "r") as file:
        lines = file.readlines()
        if len(lines) != 1:
            raise inputerrors.InvalidTemplateException(str(fileName))
        templateText = lines[0]

    randomVars = [randint(0, 255) for var in findall(r"\{\{ (r\[[0-9]\]) \}\}", templateText)]

    env = Environment(loader=FileSystemLoader(path),
                      autoescape=True)
    template = env.get_template(templateName)

    return template.render(n=dnum, r=randomVars)