import socket
import argparse

HOST = '192.168.100.92'

def echo_client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HOST, port)
    print(f"Menghubungkan ke {HOST} port {port}...")
    sock.connect(server_address)
    
    try:
        while True:
            message = input("Masukkan pesan: ")
            sock.sendall(message.encode('utf-8'))
            
            if message.lower() == "exit":
                print("Menutup koneksi ke server.")
                break
            
            data = sock.recv(1024)
            print(f"Server mengembalikan: {data.decode('utf-8')}")
    
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    
    finally:
        sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Echo Client")
    parser.add_argument('--port', type=int, required=True)
    args = parser.parse_args()
    echo_client(args.port)