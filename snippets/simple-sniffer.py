#!/bin/env python3
from scapy.all import *

def print_pkt(pkt):
    print(pkt.summary())

pkt = sniff(iface='enp5s0', filter='icmp', prn=print_pkt)