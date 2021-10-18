# via Black Hat Python Second Edition

import argparse
import shlex
import socket
import subprocess
import sys
import textwrap
import threading


def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd),
                                     stderr=subprocess.STDOUT)
    return output.decode()


class NetCat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()

    def send(self):
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(buffer)
        try:
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    # If received data is less than the 4096 chunk size, this is the
                    # last chunk, so stop
                    if recv_len < 4096:
                        break
                if response:
                    print(response)
                    buffer = input('> ')
                    buffer += '\n'
                    self.socket.send(buffer.encode())
        except KeyboardInterrupt:
            print('Terminated by keyboard interrupt.')
            self.socket.close()
            sys.exit()

    def listen(self):
        print(f'Listening on {self.args.target}:{self.args.port}')
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)
        while True:
            client_socket, client_address = self.socket.accept()
            client_thread = threading.Thread(target=self.respond_to_incoming,
                                             args=(client_socket,
                                                   client_address))
            client_thread.start()

    def respond_to_incoming(self, client_socket, client_address):
        if self.args.execute:
            output = execute(self.args.execute)
            client_socket.send(output.encode())
        elif self.args.upload:
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)
                if data:
                    file_buffer += data
                else:
                    break
            with open(self.args.upload, 'wb') as uploaded_file:
                uploaded_file.write(file_buffer)
            message = f'Saved file {self.args.upload}'
            client_socket.send(message.encode())
        elif self.args.command:
            cmd_buffer = b''
            while True:
                try:
                    client_socket.send(b'#> ')
                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += client_socket.recv(64)
                    response = execute(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''
                except Exception as exception:
                    print(f'server killed {exception}')
                    self.socket.close()
                    sys.exit()


def main():
    p = argparse.ArgumentParser(description='Network Utility',
                                epilog=textwrap.dedent('''Examples:
    nc.py -t 192.168.1.111 -p 4444 -l -c # command shell
    nc.py -t 192.168.1.111 -p 4444 -l -u=mytest.txt # upload to file
    nc.py -t 192.168.1.111 -p 4444 -l -e=\"cat /etc/passwd\" # execute command
    echo 'HELLO' | nc.py -t 192.168.1.111 -p 4444 # echo txt to server port 4444
    nc.py -t 192.168.1.111 -p 4444 # connect to server'''))

    p.add_argument('-c',
                   '--command',
                   action='store_true',
                   help='command shell')
    p.add_argument('-e', '--execute', help='execute command')
    p.add_argument('-l', '--listen', action='store_true', help='listen')
    p.add_argument('-p', '--port', type=int, default=4444, help='port')
    p.add_argument('-t',
                   '--target',
                   default='192.168.1.111',
                   help='target IP address')
    p.add_argument('-u', '--upload', help='upload file')
    args = p.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()

    nc = NetCat(args, buffer.encode())
    nc.run()


if __name__ == '__main__':
    main()
