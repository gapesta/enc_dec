from cryptography.fernet import Fernet

# Membuat kunci enkripsi
key = Fernet.generate_key()

# Menyimpan kunci ke dalam file
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)
