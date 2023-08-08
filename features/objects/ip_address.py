import ipaddress

def createIPAddress(address, prefixLength):
    return ipaddress.ip_network(f"{address}/{prefixLength}")