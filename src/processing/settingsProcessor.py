import yaml

class settingsProcessor():
    def __init__(self, settingsFile):
        with open(settingsFile, "r") as settings:
            self.settings = yaml.load(settings, Loader=yaml.Loader)