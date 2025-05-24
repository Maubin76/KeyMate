from cryptography.fernet import Fernet
from config import ENCRYPTION_KEY

# Crée un Fernet pour le chiffrement/déchiffrement
fernet = Fernet(ENCRYPTION_KEY)

def encrypt(data: bytes) -> bytes:
    return fernet.encrypt(data)

def decrypt(token: bytes) -> bytes:
    return fernet.decrypt(token)
