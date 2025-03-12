import socket
import argparse
import threading

HOST = '192.168.100.92'
BUFFER_SIZE = 1024

def handle_client(client_socket, client_address):
    """Handles communication with a single client."""
    print(f"Terhubung dengan {client_address}")
    
    while True:
        try:
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break

            message = data.decode('utf-8')
            print(f"Pesan dari {client_address}: {message}")

            if message.lower() == "exit":
                print(f"Client {client_address} meminta untuk mengakhiri koneksi.")
                client_socket.sendall("Koneksi ditutup oleh server.".encode('utf-8'))
                break
            
            client_socket.sendall(data)  # Echo the message back to client
        
        except ConnectionResetError:
            print(f"Client {client_address} terputus secara paksa.")
            break

    client_socket.close()
    print(f"Koneksi dengan {client_address} ditutup.")

def echo_server(port):
    """Main server function to handle multiple clients."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (HOST, port)
    sock.bind(server_address)
    sock.listen(5)
    
    print(f"Server berjalan di {HOST} port {port}...")

    while True:
        client_socket, client_address = sock.accept()
        
        # Create a new thread for each connected client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multi-Client Echo Server")
    parser.add_argument('--port', type=int, required=True, help="Port untuk server")
    args = parser.parse_args()
    echo_server(args.port)