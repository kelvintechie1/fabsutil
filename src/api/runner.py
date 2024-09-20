"""Runner module to execute API calls, abstracting API platform"""
from src.errors import apierrors, processingerrors
from . import cmlapi, evengapi, gns3api

class apirunner():
    """API runner class within runner module"""
    def __init__(self, settings):
        try:
            platform = settings["lab"]["platform"]
            apis = {"cml": cmlapi, "eveng": evengapi, "gns3": gns3api}
            if platform not in apis:
                raise KeyError("platform")
            else:
                self.emulator = apis[platform]

        except KeyError as e:
            raise processingerrors.SettingNotFoundError(e) from e

        self.devices = None
        self.links = None
        self.ports = None

    def runBaseAPIOperations(self):
        """Run API operations that exist in all network emulator platforms
        Currently - building topology (node/device/port data)"""

        self.emulator.authAPI()
        self.devices = self.emulator.buildDevicesList()
        self.links = self.emulator.buildLinksList()
        self.ports = [self.emulator.buildPortsList(device) for device in self.devices]

    def runCMLAPIOperations(self):
        """Run API operations specific for CML"""

        # Create PATty associations
        portRange = (num for num in range(7200, 7300)) # Port range for console access, may add ability to change via config later
        for device in self.devices:
            device["port"] = next(portRange)
            device.assignConsoleTelnetPort(device["id"], device["port"])
