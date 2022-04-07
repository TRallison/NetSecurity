import sys
from scapy.all import *
def main(args):
    if len(args) > 0:
        arg1 = args[0]
    if arg1:
        a = IP(dst=arg1)
        print([p for p in a])
        scapy_data = sr1(IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=arg1)))
        print(scapy_data[DNS].summary())
if __name__ == "__main__":
    main(sys.argv[1:]) 
