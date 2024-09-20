"""Runner module to execute API calls, abstracting API platform"""
from src.errors import processingerrors
from . import cmlapi, evengapi, gns3api

class apirunner():
    """API runner class within runner module"""
    def __init__(self, platform, **kwargs):
        try:
            self.emulator = {"cml": cmlapi.CMLAPI, "eveng": evengapi.EVENGAPI, "gns3": gns3api.GNS3API}[platform](**kwargs)
        except KeyError as e:
            raise processingerrors.SettingNotFoundError("platform") from e

        self.devices = None
        self.links = None
        self.ports = None

        self.runBaseAPIOperations()
        match self.emulator:
            case cmlapi.CMLAPI():
                self.runCMLAPIOperations()
            case evengapi.EVENGAPI():
                pass
            case gns3api.GNS3API():
                pass

    def runBaseAPIOperations(self):
        """Run API operations that exist in all network emulator platforms
        Currently - building topology (node/device/port data)"""

        self.emulator.authAPI()
        self.devices = self.emulator.buildDevicesList()
        self.links = self.emulator.buildLinksList()
        self.ports = [self.emulator.buildPortsList(device["id"]) for device in self.devices]

    def runCMLAPIOperations(self):
        """Run API operations specific for CML"""

        # Create PATty associations
        portRange = (num for num in range(7200, 7300)) # Port range for console access, may add ability to change via config later
        for device in self.devices:
            device["port"] = next(portRange)
            self.emulator.assignConsoleTelnetPort(device["id"], device["port"])
