#!/bin/env python3
import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(('127.0.0.1', 9090))

tcp.sendall(b"Hello from simple tcp client.\n")
tcp.sendall(b"Hello again from simple tcp client.\n")

# Uncomment to see message returned from simple-tcp-server.py
# print(tcp.recv(1024).decode('utf-8'))

tcp.close()
