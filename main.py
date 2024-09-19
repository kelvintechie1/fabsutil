from urllib3 import disable_warnings
disable_warnings()

import click as cl
import src.processing.settingsProcessor as settingsProcessor

if __name__ == "__main__":
    settingsProcessor.settingsProcessor("data/user/settings.yaml")