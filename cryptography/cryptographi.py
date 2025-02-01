import os
import platform
from cryptography.fernet import Fernet

class FileEncryptor:
    def __init__(self, key_file=None):
        # Sesuaikan path file kunci berdasarkan platform
        default_key_file = "key.key"
        if platform.system() == "Linux":
            default_key_file = "./key.key"
        elif platform.system() == "Windows":
            default_key_file = "C:\\key.key"
        elif platform.system().startswith("Android"):
            default_key_file = "/sdcard/key.key"
        
        self.key_file = key_file or default_key_file
        self.key = None
        if os.path.exists(self.key_file):
            self.load_key()

    def load_key(self):
        """Load the encryption key from the key file."""
        with open(self.key_file, "rb") as f:
            self.key = f.read()
        print(f"Key loaded from {self.key_file}")
        self.fernet = Fernet(self.key)

    def create_key(self):
        """Create and save a new encryption key."""
        self.key = Fernet.generate_key()
        with open(self.key_file, "wb") as f:
            f.write(self.key)
        print(f"New key generated and saved to {self.key_file}")
        self.fernet = Fernet(self.key)

    def delete_key(self):
        """Delete the encryption key file."""
        if os.path.exists(self.key_file):
            os.remove(self.key_file)
            self.key = None
            self.fernet = None
            print(f"Key file {self.key_file} has been deleted.")
        else:
            print("No key file found to delete.")

    def encrypt_file(self, file_path, output_path=None):
        """Encrypt a single file."""
        if not self.key:
            print("No key loaded. Please create or load a key first.")
            return
        if not output_path:
            output_path = file_path + ".enc"

        with open(file_path, "rb") as f:
            data = f.read()

        encrypted_data = self.fernet.encrypt(data)

        with open(output_path, "wb") as f:
            f.write(encrypted_data)

        print(f"File encrypted: {file_path} -> {output_path}")

    def decrypt_file(self, file_path, output_path=None):
        """Decrypt a single file."""
        if not self.key:
            print("No key loaded. Please create or load a key first.")
            return
        if not output_path:
            output_path = file_path.replace(".enc", "")

        with open(file_path, "rb") as f:
            encrypted_data = f.read()

        decrypted_data = self.fernet.decrypt(encrypted_data)

        with open(output_path, "wb") as f:
            f.write(decrypted_data)

        print(f"File decrypted: {file_path} -> {output_path}")

    def encrypt_folder(self, folder_path, output_folder=None):
        """Encrypt all files in a folder."""
        if not self.key:
            print("No key loaded. Please create or load a key first.")
            return
        if not output_folder:
            output_folder = folder_path + "_encrypted"

        os.makedirs(output_folder, exist_ok=True)

        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_path)
                output_path = os.path.join(output_folder, relative_path + ".enc")
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                self.encrypt_file(file_path, output_path)

        print(f"Folder encrypted: {folder_path} -> {output_folder}")

    def decrypt_folder(self, folder_path, output_folder=None):
        """Decrypt all files in an encrypted folder."""
        if not self.key:
            print("No key loaded. Please create or load a key first.")
            return
        if not output_folder:
            output_folder = folder_path.replace("_encrypted", "_decrypted")

        os.makedirs(output_folder, exist_ok=True)

        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_path)
                output_path = os.path.join(output_folder, relative_path.replace(".enc", ""))
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                self.decrypt_file(file_path, output_path)

        print(f"Folder decrypted: {folder_path} -> {output_folder}")

