from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import AES
import socket
import pickle

host = "127.0.0.1"
port = 5555
start = False
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rand = Random.new().read
key = RSA.generate(1024,rand)
public_key = key.publickey()

if not start:
    data = pickle.dumps(public_key)
    s.connect((host,port))
    s.send(data)
    data = s.recv(4096)
    data = pickle.loads(data)
    # Decrypt AES key with private key
    AES_KEY = key.decrypt(data)
    cipher = AES.new(AES_KEY, AES.MODE_CFB, AES_KEY)
    start = True

while start:
    data = input('Enter your message: ')
    data = cipher.encrypt(data)
    data = pickle.dumps(data)
    s.send(data)
    data = s.recv(1024)
    data = pickle.loads(data)
    decrypted = cipher.decrypt(data)
    print("\nServer -> %s\n" % decrypted)
