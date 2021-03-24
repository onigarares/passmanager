from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64


# gAAAAABgSUX
# gAAAAABgSUY
# gAAAAABgSUY
# gAAAAABgSUY
# gAAAAABgSUT
# gAAAAABgSUa
# gAAAAABgSUb
# gAAAAABgSUd
# gAAAAABgSUT
# gAAAAABgSUh
# gAAAAABgSUi
# gAAAAABgSUk




def encrypt(master_pass,password):

    #Return eccrypted pssword as a string  
    master_pass = bytes(master_pass, 'utf-8')
    password = bytes(password, 'utf-8')

    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b"cocojambo", iterations=1000, backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(master_pass))
    f = Fernet(key)
    encrypted = f.encrypt(password)
    return (encrypted.decode())

def decrypt(master_pass,encrypted):

    #Return decrypted password as a string
    master_pass = bytes(master_pass, 'utf-8')
    encrypted = bytes(encrypted, 'utf-8')

    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b"cocojambo", iterations=1000, backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(master_pass))
    f = Fernet(key)
    decrypted = f.decrypt(encrypted)

    return (decrypted.decode())

if __name__ == '__main__':
    
   master_pass = 'Test1234'
   password1 = 'parola'
   password2 = 'parola2'

   print(encrypt(master_pass,password1))
