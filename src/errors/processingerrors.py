"""Input Data Processing Errors"""
class SettingNotFoundError(Exception):
    """Exception to be raised when a required setting is not available or assumes an invalid error"""
    def __init__(self, setting):
        super().__init__(f"{setting} not found in settings.yaml file or assumes invalid value")

class SettingCredentialNotFoundError(Exception):
    """Exception to be raised when emulatorUser and emulatorPass is not available in the settings.yaml"""
    def __init__(self):
        super().__init__("Emulator Username/password not found in settings.yaml file")

class RuntimeCredentialNotFoundError(Exception):
    """Exception to be raised when the runtime emulatorAuthMethod is selected and 
    username/password is not provided through the CLI"""
    def __init__(self):
        super().__init__("Username/password not provided through CLI and runtime emulatorAuthMethod selected. Configure another emulatorAuthMethod or use the username/password flags to pass credentials to FABS")

class EnvCredentialNotFoundError(Exception):
    """Exception to be raised when the env emulatorAuthMethod is selected and 
    username/password is not provided through the required environment variables"""
    def __init__(self):
        super().__init__("FABS_EMULATOR_USERNAME and/or FABS_EMULATOR_PASSWORD environment variables not found and env emulatorAuthMethod selected")
