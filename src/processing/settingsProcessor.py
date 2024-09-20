"""Process settings.yaml file"""
import yaml
from src.errors import processingerrors

def loadSettings(settingsFile):
    """Load settings from YAML file"""
    try:
        with open(settingsFile, encoding="utf-8", mode="r") as settings:
            return yaml.load(settings, Loader=yaml.Loader)
    except FileNotFoundError:
        print(f"settings.yaml file not found at the specified location: {settingsFile}")
    except yaml.YAMLError:
        print("settings.yaml file is not formatted with the correct YAML format.")

def validateMandatorySettingsExist(settings: dict):
    """Validate that all mandatory settings exist in the settings.yaml file"""
    mandatorySettings = {"lab": ["platform", "emulatorAddress", "emulatorAuthMethod", "labId"]}
    missingSettings = []

    for settingType, settingValues in mandatorySettings.items():
        for setting in settingValues:
            if setting not in settings["settings"][settingType]:
                missingSettings.append(settings)

    if missingSettings:
        raise processingerrors.SettingNotFoundError(", ".join(missingSettings))

    return settings
