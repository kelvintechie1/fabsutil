from pathlib import Path
import yaml

def readSettings():
    with open((Path(__file__).parents[1] / "data" / "user" / "settings.yaml").resolve(), "r") as file:
        return yaml.load(file, Loader=yaml.FullLoader)