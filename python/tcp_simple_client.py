import socket

host = '192.168.1.155'
port = 9998

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))
sock.send(b'Hello, world!\n')
while (True):
    msg = sock.recv(4096)
    if not msg:
        break
    print(msg.decode("utf-8"))

sock.close()
