#!/usr/bin/env python3

import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048

def echo_client(port):
    # Membuat socket object menggunakan UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (host, port)

    print("Connecting to %s port %s" % server_address)
    message = 'This is the message. It will be repeated.'

    try:
        # Mengirim pesan ke server
        message = "Good Morning!!! This will be echoed"
        print("Sending %s" % message)
        sent = sock.sendto(message.encode('utf-8'), server_address)

        # Menerima balasan dari server
        data, server = sock.recvfrom(data_payload)
        print("received %s" % data.decode('utf-8'))

    finally:
        print("Closing connection to the server")
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Client Example')
    parser.add_argument('--port', action="store", dest="po