import json
from config import ENC_FILE
from crypto import encrypt, decrypt
import os

def load_passwords():
    if not os.path.exists(ENC_FILE):
        return {}
    with open(ENC_FILE, "rb") as f:
        encrypted_data = f.read()
    if not encrypted_data:
        return {}
    decrypted_data = decrypt(encrypted_data)
    return json.loads(decrypted_data)

def save_passwords(passwords):
    data = json.dumps(passwords).encode()
    encrypted_data = encrypt(data)
    with open(ENC_FILE, "wb") as f:
        f.write(encrypted_data)

def add_password(name, password):
    passwords = load_passwords()
    passwords[name] = password
    save_passwords(passwords)

def get_password(name):
    passwords = load_passwords()
    return passwords.get(name, None)
