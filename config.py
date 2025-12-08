from pathlib import Path
from error import USB_key_not_found_error
# global configuration for the password manager
# -*- coding: utf-8 -*-
USB_KEY_PATH = Path("E:") / "KeyMate"

def read_file_on_usb_key(filename: str):
    """Reads a file from the USB key."""
    if not USB_KEY_PATH.exists():
        USB_key_not_found_error()
        raise FileNotFoundError(f"Please insert the USB key")
    
    with open(USB_KEY_PATH / filename, "rb") as file:
        return file.read()

MASTER_PASSWORD =  read_file_on_usb_key("master_password.hash").decode() # SHA-256 hash of the master password
ENCRYPTION_KEY = read_file_on_usb_key("encryption_key.enc") # 32 bytes for AES-256
ENC_FILE = Path.home() / "OneDrive" / "KeyMate" / "passwords.enc" # File to store encrypted passwords
