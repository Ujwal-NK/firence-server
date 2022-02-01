# import required module
from cryptography.fernet import Fernet
import json

def get():
    # def get_json():
    key = ""

    # opening the key
    with open('../data/filekey.key', 'rb') as filekey:
        key = filekey.read()

    # using the key
    fernet = Fernet(key)

    # opening the encrypted file
    with open('../data/mail.crpt', 'rb') as enc_file:
        encrypted = enc_file.read()

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)

    return json.loads(decrypted.decode())
