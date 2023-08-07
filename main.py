from urllib3 import disable_warnings
disable_warnings()

import re
from api import apicaller
from lab import device
from input import readSettings, templateparser
from errors import *
from features.config import config_loopback_ipaddressing

def main():
    # Configure app settings
    settings = readSettings.readSettings()

    try:
        # Create API session
        api = apicaller.createAuthedAPISession(settings["general"]["url"], settings["general"]["trustcert"])
        # Gather data about lab objects (devices, links, interfaces, etc.) from API
        allDevices = api.buildDevicesList(settings["platform"]["lab_id"])
        links = api.buildLinksList(settings["platform"]["lab_id"])
        interfaces = [api.buildInterfacesList(settings["platform"]["lab_id"], device["id"])
                    for device in allDevices]
    except apierrors.APIError as e:
        print(e.message)
        exit(-1)
    
    # Create the device objects for the lab
    devices = device.buildSupportedDevices(allDevices, interfaces, links,
                                           settings["platform"]["appliance"])
    

    print(config_loopback_ipaddressing.createIPAddress(
        templateparser.parseIPAddressPattern(
        settings["interfaces"]["loopback"]["router_id"]["pattern"],
        "100"), settings["interfaces"]["loopback"]["router_id"]["prefix_length"]))
    
if __name__ == "__main__":
    main()