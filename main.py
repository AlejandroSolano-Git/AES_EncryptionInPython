from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

salt = b'\xf8%\x85\xb1\x9a\xe1\xb3\xae\xda\x99V_\xe5^\xaa=\x9c\xcb\xc0\xb2\x16\xb5\xce\xf7\x03`\xa2\x19{\xe7\x99*'
password = input("Enter a password for the key: ")

key = PBKDF2(password, salt, dkLen=32)

message = input("Enter a message to encrypt: ").encode('ASCII')

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

with open('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)

with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)

with open('key.bin', 'wb') as f:
    f.write(key)