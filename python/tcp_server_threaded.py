import socket
import threading

IP = '192.168.1.155'
PORT = 9998


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((IP, PORT))
    sock.listen(5)
    print(f"[*] Listening on {IP}:{PORT}")

    while True:
        client_sock, address = sock.accept()
        client_processor = threading.Thread(target=process_client,
                                            args=(client_sock, address))
        client_processor.start()


def process_client(client_sock, address):
    print(f'[*] Accepted connection from {address[0]}:{address[1]}')
    request = client_sock.recv(1024)
    print(f'[*] Received: {request.decode("utf-8")}')
    client_sock.send(b"OK")


if __name__ == '__main__':
    main()
