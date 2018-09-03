import socket
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
import string
import random

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8080

def encrypt_AES_KEY(KEY):
    publickey = ""
    encryptor = RSA.importKey(publickey)
    encryptor.encrypt(KEY, 0)
    return encriptedData[0]

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((SERVER_IP, SERVER_PORT))
    s.listen(1)
    print '[+] Listening for incoming TCP connections...'
    conn, addr = s.accept()
    print '[+] Connection from: ' + addr
    global key
    key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(32))
    print "Generated AES key: " + str(key)
    conn.send(encrypt_AES_KEY(key))
    global counter
    counter = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:;<>|\\') for _ in range(16))
    conn.send(encrypt_AES_KEY(counter))

