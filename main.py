"""Main module for the FABS Utility"""
from pathlib import Path
from src.processing.settingsProcessor import loadSettings
from src.processing.credsProcessor import credsProcessor
import click as cli

from urllib3 import disable_warnings
disable_warnings()

@cli.group(invoke_without_command=True, context_settings=dict(help_option_names=["-?", "--help"]))
@cli.option("-c", "--config-file", type=cli.Path(dir_okay=False), required=False,
            help="Define the location of the settings.yaml configuration file",
            default="data/user/settings.yaml", show_default=True)
@cli.option("-u", "--emulator-username", required=False, type=str)
@cli.option("-p", "--emulator-password", required=False,
            prompt="Enter your password for network emulator access",
            hide_input=True, prompt_required=False, type=str)
def main(config_file, emulator_username, emulator_password):
    """Forget About the Boring Stuff (FABS) Utility - Automating your lab configs!"""
    settings = loadSettings(Path(config_file).absolute())
    creds = credsProcessor(emulator_username, emulator_password, settings)



if __name__ == "__main__":
    main()
