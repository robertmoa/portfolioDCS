from cryptography.fernet import Fernet

#generates the intial key
def genkey():
    key = Fernet.generate_key()
    with open("thekey.key", "wb") as key_file:
        key_file.write(key)

def loadkey():
    return open("thekey.key","rb").read()

#checks if key exists, if not key is generated
try:
    with open("thekey.key", 'rb') as f:
        pass
except FileNotFoundError:
    print("Fernet key not found, generating...")
    genkey()
key = loadkey()
f = Fernet(key)
print("This is a simple program to encrypt and decrypt files with fernet")
print("To use, place files in this directory, then use the options below")
print("E <filename> to encrypt, D <filename> to decrypt")
while True:
    userinput = input("What would you like to do: ")
    if (userinput[0] =="E"):
        try:
            with open(userinput[2:],"rb") as filetoencrypt:
                filedata = filetoencrypt.read()
                encryptedfiledata = f.encrypt(filedata)
            with open(userinput[2:],"wb") as filetoencrypt:
                filetoencrypt.write(encryptedfiledata)
            print("File successfuly encrypted!")
        except FileNotFoundError:
            print("File not found, make sure you entered it correctly")


    elif (userinput[0] =="D"):
        try:
            with open(userinput[2:],"rb") as filetodecrypt:
                encryptedfiledata = filetodecrypt.read()
                decryptedfiledata = f.decrypt(encryptedfiledata)
            with open(userinput[2:],"wb") as filetodecrypt:
                filetodecrypt.write(decryptedfiledata)
            print("File successfuly decrypted!")
        except FileNotFoundError:
            print("File not found, make sure you entered it correctly")

    else:
        print("Command not recognised, make sure it is correct and retry")







