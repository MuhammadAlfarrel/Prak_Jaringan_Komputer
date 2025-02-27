#!/usr/bin/env python3

import socket
import sys
import argparse

host = '192.168.10.8'
data_payload = 2048

def echo_server(port):
    # Membuat socket object menggunakan UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (host, port)
    
    print("Starting up echo server on %s port %s" % server_address)
    # Bind the socket, menentukan port yang digunakan pada host tujuan
    sock.bind(server_address)

    while True:
        # Menunggu menerima pesan dari client
        print("Waiting to receive message from client")
        data, address = sock.recvfrom(data_payload)
        print("received %s bytes from %s" % (len(data), address))
        print("Data: %s" % data.decode('utf-8'))

        if data:
            # Server mengirim pesan ke client
            sent = sock.sendto(data, address)
            print("sent %s bytes back to %s" % (sent, address))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)
