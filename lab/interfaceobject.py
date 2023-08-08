from features.objects import ip_address

class IPInterface:
    def __init__(self, intType, intPrefix, intNum, ipAddresses):
        self.intType = intType
        self.intPrefix = intPrefix
        self.intNum = intNum
        self.ipAddresses = [ip_address.createIPAddress(ipAddresses[0], ipAddresses[1])]