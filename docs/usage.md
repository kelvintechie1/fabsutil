# FABS Usage

## FABS Execution
### Before you run FABS...

FABS relies on a number of dependent Python libraries for its functionality. These libraries need to be installed via `pip` before you proceed. Otherwise, FABS will likely throw `ModuleNotFoundError` exceptions.

The recommended method is to use a Python virtual environment (venv). On Unix-based systems (e.g., macOS/Linux), use the following commands to create a venv called `fabsutil-venv` in your terminal's default directory (usually your home directory) and install the requisite packages.
```bash
python -m venv fabsutil-venv # YOU MAY NEED TO USE python3 INSTEAD OF python, if python points to a Python 2 installation
source fabsutil-venv/bin/activate
python -m pip install -r requirements.txt
```

The steps on Windows are identical, except the `source` command is replaced by the execution of the `Activate.ps1` PowerShell script found in the same location. Reference Python documentation for more information on virtual environments.

### How to run FABS

To run FABS, just use the `main.py` file in the root directory! All other Python files located within the FABS directories will automatically be referenced by `main.py` as necessary.

By running `python main.py`, you will accept all of the default settings. Reference the [FABS Defaults](#fabs-defaults) section for more. Settings overrides are passed to FABS through command-line arguments/flags. More information is available in the CLI through the `python main.py [-h|--help]` commands and in the [FABS Command-Line Flags](#fabs-command-line-flags) section of this document.

### FABS Command-Line Flags

The following table contains usage instructions for the command-line flags included in FABS. To use any of these flags, include them after `main.py` (e.g., `python main.py --help` to use the `--help` flag.)

| Flag | Description |
| ---- | ----------- |
| `-h` or `--help` | Display information about the flags in the CLI |
| `-c` or `--config-file` | Override the default location for the `settings.yaml` file (default is in the `data/user` folder)

## FABS Defaults
### Default settings.yaml file location
By default, FABS will assume the relative path `data/user/settings.yaml` for the settings.yaml file location, based on the main fabsutil directory. This means that it doesn't matter where the fabsutil directory is stored on your system, **but** it does matter that settings.yaml is found in precisely this location within the fabsutil subdirectories.

If you would like to override this behavior, use the `-c` or `--config-file` flag when executing the `main.py` file.