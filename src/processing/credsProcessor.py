"""Process credentials for network emulator programmatic access"""
import os
from src.errors import processingerrors

def credsProcessor(cli_emulator_username, cli_emulator_password, settings):
    """Validate selected emulatorAuthMethod and return the required credentials, 
    raising exception if they are unavailable"""

    labSettings = settings["settings"]["lab"]
    try:
        match labSettings["emulatorAuthMethod"]:
            case "settings":
                creds = (labSettings["emulatorUser"], labSettings["emulatorPass"],
                         processingerrors.SettingNotFoundError)
            case "env":
                creds = (os.environ.get("FABS_EMULATOR_USERNAME"),
                         os.environ.get("FABS_EMULATOR_PASSWORD"),
                         processingerrors.EnvCredentialNotFoundError)
            case "runtime":
                creds = (cli_emulator_username, cli_emulator_password,
                         processingerrors.RuntimeCredentialNotFoundError)

        if not (creds[0] and creds[1]):
            raise creds[2]

        return creds[0:1]

    except KeyError as e:
        raise processingerrors.SettingNotFoundError(e) from e
