import argparse
import shlex
import socket
import subprocess
import sys
import threading

class server:
    def __init__(self, args):
        self.host = args.host
        self.port = args.port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def exec(self, cmd):
        return subprocess.check_output(shlex.split(cmd))

    def respond(self, client):
        buff = ''
        while True:
            try:
                client.send(b'> ')
                while '\n' not in buff:
                    input = client.recv(64).decode()
                    client.send(input.encode())
                    buff += input
                if buff:
                    client.send(buff.encode())
                    buff = ''
            except Exception as e:
                print(f'Server exception: {e}')
                self.sock.close()
                sys.exit()          

    def listen(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen(4)
        while True:
            client, _ = self.sock.accept()
            thread = threading.Thread(target=self.respond, args=(client,))
            thread.start()
    
def main():
    p = argparse.ArgumentParser()
    p.add_argument('--host', help="server address")
    p.add_argument('--port', type=int, help="server port")
    args = p.parse_args()
    serv = server(args)
    serv.listen()

if __name__ == '__main__':
    main()
