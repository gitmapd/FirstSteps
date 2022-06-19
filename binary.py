import numpy as np

def Str2IPV4(s):
  return np.array(s.split('.'), dtype=np.uint8)

def NetAddress(ipadd, netmask):
  return Str2IPV4(ipadd) & Str2IPV4(netmask)

def IPV42Str(ipv4):
  return '.'.join(ipv4.astype(str))

def WildCard(subnetmask):
    return ~Str2IPV4(subnetmask)

def BroadCast(subnetmask,netaddress):
    return ~Str2IPV4(subnetmask) | Str2IPV4(netaddress)



