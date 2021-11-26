#!usr/bin/python3

#importing libraries

import socket
from termcolor import colored

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.settimeout(5)

host = input("[+] Enter a host to scan: ") # 192.168.1.7
#port = int(input("[+] Enter a port a scan: ")) #445

def portScan(port):
    if socket.connect_ex((host, port)):
        print(colored(f"[!!] Port {port} on {host} is closed", 'red'))
    else:
        print(colored(f"[+] Port {port} on Host {host} is open", "green"))

#if we want to scan a whole range of ports then lets change a few lines in the code!

for port in range(1, 1000):
    portScan(port)
    #this will allow the scannng to take place in the assigned ip addr and a range of ports between 1-100!

