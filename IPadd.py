import numpy as np
from argparse import ArgumentParser
def Str2IPV4(s):
        return np.array(s.split('.'),dtype=np.uint8)

if __name__=='__main__':
    ap=ArgumentParser(description='Enter IP and Mask')
    ap.add_argument('--IP',help='Enter IP')
    ap.add_argument('--MASK', help='Enter MASK')
    args=ap.parse_args()
    if args.IP and args.MASK is not None:
        print(f"{Str2IPV4(args.IP)}, {Str2IPV4(args.MASK)}")
