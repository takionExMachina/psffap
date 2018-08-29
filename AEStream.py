import os
from Crypto.Cipher import AES

counter = os.urandom(16)
key = os.urandom(32)

enc = AES.new(key, AES.MODE_CTR, counter=lambda:counter)
encrypted = enc.encrypt("message"*4)
print encrypted

dec = AES.new(key, AES.MODE_CTR, counter=lambda:counter)
decrypted = dec.decrypt(encrypted)
print decrypted

