#make string encryption in python

#generate a key

from cryptography.fernet import Fernet

def make_key():

    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)


def read_key():

    with open("key.key","rb") as key_file:
        return key_file.read()
    
# make_key()
key = read_key()

message ="encrypt me".encode()

f = Fernet(key)

encrypted = f.encrypt(message)

print(encrypted)

decrypted = f.decrypt(encrypted)

print("\n")

print(decrypted)

#encrypt a file

def encrypted(filename,key):



    f = Fernet(key)
    with open(filename,'rb') as file:
        data = file.read()
        encrypted_data = f.encrypt(data)

    with open(filename,'wb') as file:
        file.write(encrypted_data)


def decrypted(filename,key):
    f = Fernet(key)
    with open(filename,'rb') as file:
        encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
    with open(filename,'wb') as file:
        file.write(decrypted_data)

key = read_key()

encrypted('sample.txt',key)

decrypted('sample.txt',key)







