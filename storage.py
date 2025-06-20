import json
from config import ENC_FILE
from crypto import encrypt, decrypt
import os

def load_passwords():
    if not os.path.exists(ENC_FILE):
        return []
    with open(ENC_FILE, "rb") as f:
        encrypted_data = f.read()
    if not encrypted_data:
        return []
    decrypted_data = decrypt(encrypted_data)
    return json.loads(decrypted_data)

def save_passwords(passwords_list):
    data = json.dumps(passwords_list, indent=4).encode()
    encrypted_data = encrypt(data)
    with open(ENC_FILE, "wb") as f:
        f.write(encrypted_data)

def add_password(site, id_value, password_value):
    passwords = load_passwords()
    # Vérifier si le site existe déjà et remplacer si besoin
    for entry in passwords:
        if entry["site"] == site:
            entry["id"] = id_value
            entry["password"] = password_value
            break
    else:
        passwords.append({"site": site, "id": id_value, "password": password_value})
    save_passwords(passwords)

def get_password(site):
    passwords = load_passwords()
    for entry in passwords:
        if entry["site"] == site:
            return entry  # Retourne l'entrée complète
    return None

def get_all_passwords():
    return load_passwords()

def delete_password(site):
    passwords = load_passwords()
    passwords = [entry for entry in passwords if entry["site"] != site]
    save_passwords(passwords)

def update_password(site, new_id, new_password):
    passwords = load_passwords()
    for entry in passwords:
        if entry["site"] == site:
            entry["id"] = new_id
            entry["password"] = new_password
            break
    save_passwords(passwords)
