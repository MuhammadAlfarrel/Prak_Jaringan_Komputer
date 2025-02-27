#!/usr/bin/env python3

import socket
import sys
import argparse

host = '192.168.10.8'
data_payload = 2048
backlog = 5

def echo_server(port):
    # Membuat socket object dengan TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)

    print("Starting up echo server on %s port %s" % server_address)

    # Bind the socket, Menentukan port yang digunakan pada host tujuan
    sock.bind(server_address)

    # Listen for incoming connection from clients, Nilai backlog menentukan jumlah maksimum antrian koneksi
    sock.listen(backlog)

    while True:
        print("Waiting to receive message from client")
        # Establish a connection, menunggu koneksi dari client
        client, address = sock.accept()

        # Server menerima data dari client
        data = client.recv(data_payload)

        if data:
            print("Data: %s" % data.decode('utf-8'))

            # Server mengirim data ke client
            client.send(data)
            print("sent %s bytes back to %s" % (data.decode('utf-8'), address))

        # Koneksi berakhir
        client.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)
