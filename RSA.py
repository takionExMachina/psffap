from Crypto.PublicKey import RSA

new_key = RSA.generate(4096)

public_key = new_key.publickey().exportKey("PEM")
private_key = new_key.exportKey("PEM")

def save(name, content):
    f = open(name, "wb")
    f.write(content)
    f.close()

print private_key
print public_key

save('private.pem', private_key)
save('public.pem', public_key)
