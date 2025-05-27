from cryptography.fernet import Fernet
from config import ENCRYPTION_KEY, MASTER_PASSWORD
import hashlib

# Crée un Fernet pour le chiffrement/déchiffrement
fernet = Fernet(ENCRYPTION_KEY)

def encrypt(data: bytes) -> bytes:
    """Encrypt data using the Fernet key."""
    return fernet.encrypt(data)

def decrypt(token: bytes) -> bytes:
    """Decrypt a token using the Fernet key."""
    return fernet.decrypt(token)

def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def is_password_correct(provided_password: str) -> bool:
    """Verify a password against a stored hash."""
    return MASTER_PASSWORD == hash_password(provided_password)