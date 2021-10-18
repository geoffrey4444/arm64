import socket

IP = '0.0.0.0'
PORT = 9998


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((IP, PORT))
    sock.listen(5)
    print(f"[*] Listening on {IP}:{PORT}")

    while True:
        client_sock, address = sock.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        request = client_sock.recv(1024)
        print('[*] Received: (request.decode("utf-8"))')
        client_sock.send(b"OK")


if __name__ == '__main__':
    main()
