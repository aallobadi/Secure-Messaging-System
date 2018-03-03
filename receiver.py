from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import AES
import socket
import pickle

host = "127.0.0.1"
port = 5555
start = False
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
conn, addr = s.accept()

if not start:
    data = conn.recv(4096)
    public_key = pickle.loads(data)
    
    # Create AES key
    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_CFB, key)
    enc_key  = public_key.encrypt(key, 32)
    enc_dumped = pickle.dumps(enc_key)
    conn.send(enc_dumped)
    start = True
    
while start:
    data = conn.recv(1024)
    data = pickle.loads(data)
    decrypted = cipher.decrypt(data)
    print("Server -> %s" % decrypted)
    message = input("\nEnter your message: ")
    data = cipher.encrypt(message)
    data = pickle.dumps(data)
    conn.send(data)
