"""Process settings.yaml file"""
import yaml

def loadSettings(settingsFile):
    """Load settings from YAML file"""
    try:
        with open(settingsFile, encoding="utf-8", mode="r") as settings:
            return yaml.load(settings, Loader=yaml.Loader)
    except FileNotFoundError:
        print(f"settings.yaml file not found at the specified location: {settingsFile}")
    except yaml.YAMLError:
        print("settings.yaml file is not formatted with the correct YAML format.")
