#Secure-Messaging-System

sender.py create rsa key and send the publick key to reciever.py. reciever.py create AES key with AES.MODE_CFB mode and encrypt it with recieved public key and send it to the sender. Now both parties has same key they start exchange encrypted messages.
