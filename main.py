from urllib3 import disable_warnings
disable_warnings()

import re
from api import apicaller
from lab import device
from processing import readSettings, templateparser
from errors import *
from features.objects import ip_address

def main():
    # Configure app settings
    settings = readSettings.readSettings()

    if not settings["debug"]["disable_api"]:
        try:
            # Create API session
            api = apicaller.createAuthedAPISession(settings["general"]["url"], settings["general"]["trustcert"])
            # Gather data about lab objects (devices, links, ports, etc.) from API
            allDevices = api.buildDevicesList(settings["platform"]["lab_id"])
            links = api.buildLinksList(settings["platform"]["lab_id"])
            ports = [api.buildPortsList(settings["platform"]["lab_id"], device["id"])
                        for device in allDevices]
        except apierrors.APIError as e:
            print(e.message)
            exit(-1)
    
        # Create the device objects for the lab
        devices = device.buildSupportedDevices(allDevices, ports, links,
                                            settings["platform"]["appliance"])
    
    parser = templateparser.TemplateParser()
    
    for item in devices["all"]:
        item.addIPInterface("loopback", "Loopback", "0", 
                            (parser.parseIPAddressPattern
                            (settings["interfaces"]["loopback"]["router_id"]["pattern"],
                             parser.parseDeviceNumberPattern
                             (settings["devices"]["numbering"], item.name)),
                             settings["interfaces"]["loopback"]["router_id"]["prefix_length"]))
        print(f"Device {item.name}:", item.interfaces["Loopback0"].ipAddresses)
    
if __name__ == "__main__":
    main()