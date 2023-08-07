import ipaddress

def createIPAddress(parsed, prefixLength):
    return ipaddress.ip_network(f"{parsed}/{prefixLength}")