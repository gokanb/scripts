#!usr/bin/python

from socket import *
# import socket
import optparse
from threading import *
import threading

def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET , SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print(f'[+] {tgtPort}/tcp Open')
    except:
        print(f'[-] {tgtPort}/tcp Closed')
    finally:
        sock.close()


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(f'Unkown Host {tgtHost}')
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('[+] Scan results for: ' + tgtName[0])
    except:
        print('[+] Scan results for: + tgtIP')
    #settimeout(1)

    for tgtPort in tgtPorts:
        thread = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        thread.start()



def main():
    parser = optparse.OptionParser('Usage of program: ' + ' -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports seperated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPorts).split(',')
    if (tgtHost == None ) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)


if __name__ == '__main__':
    main()