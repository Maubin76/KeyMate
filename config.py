from pathlib import Path
# global configuration for the password manager
# -*- coding: utf-8 -*-
USB_KEY_PATH = Path("E:") / "KeyMate"

def read_file_on_usb_key(filename: str):
    if not USB_KEY_PATH.exists():
        raise FileNotFoundError(f"Clé USB non détectée")
    
    with open(USB_KEY_PATH / filename, "rb") as file:
        return file.read()

MASTER_PASSWORD =  read_file_on_usb_key("master_password.hash").decode() # SHA-256 hash of the master password
ENCRYPTION_KEY = read_file_on_usb_key("encryption_key.enc") # 32 bytes for AES-256
ENC_FILE = Path.home() / "OneDrive" / "KeyMate" / "passwords.enc" # File to store encrypted passwords
