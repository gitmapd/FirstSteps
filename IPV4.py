import ipaddress
class IPV4:
    def __init__(self, ipadd:ipaddress.IPv4Address):
        self.ipadd=ipadd
    def ReturnIp(self):
        return f"{self.ipadd}"



