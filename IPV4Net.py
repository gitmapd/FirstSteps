import ipaddress

class IPV4Net:
    def __init__(self,net:ipaddress.IPv4Network):
        self.net=net
    def ReturnNet(self):
        return self.net.netmask

a=IPV4Net(ipaddress.IPv4Network("192.168.0.0/24"))

print(a.ReturnNet())