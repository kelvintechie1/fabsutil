from pathlib import Path
import yaml

def readSettings():
    with open((Path(__file__).parent / "settings.yaml").resolve(), "r") as file:
        return yaml.load(file, Loader=yaml.FullLoader)