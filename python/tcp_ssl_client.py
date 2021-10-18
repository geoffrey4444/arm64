import socket
import ssl

host = 'geoffrey-lovelace.com'
port = 443

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.SSLContext(ssl.PROTOCOL_TLS)
ssock = context.wrap_socket(sock, server_hostname=host)

ssock.connect((host, port))
ssock.send(b'GET / HTTP/1.1\nHost: geoffrey-lovelace.com\n\n')
while (True):
    msg = ssock.recv(4096)
    if not msg:
        break
    print(msg.decode())

ssock.close()
