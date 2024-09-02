#!/bin/env python3 
import socket

data = b"Hello, from a simple udp client.\n"
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # SOCK_DGRAM selects the UDP type
udp.sendto(data, ("127.0.0.1", 9090)) # destination IP address and port