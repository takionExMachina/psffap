from Crypto.PublicKey import RSA

def encrypt(message):
    publickey = open("public.pem", "r")
    encryptor = RSA.importKey(publickey)
    global encryptedData
    encryptedData = encryptor.encrypt(message, 0)
    print encryptedData[0]

encrypt("sometext")

def decrypt(cipher):
    privateKey = open("private.pem", "r")
    decryptor = RSA.importKey(privateKey)
    print decryptor.decrypt(cipher)

decrypt(encryptedData)
