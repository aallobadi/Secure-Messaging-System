#Secure-Messaging-System

sender.py create rsa key and send the public key to receiver.py. receiver.py create AES key with AES.MODE_CFB mode and encrypt it with received public key and send it to the sender. Now both parties has same key they start exchange encrypted messages.
