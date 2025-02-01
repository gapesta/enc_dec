from cryptography.fernet import Fernet

# Memuat kunci dari file
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

# Inisialisasi objek Fernet dengan kunci
fernet = Fernet(key)
# Membaca file asli
with open('file.txt', 'rb') as file:
    original = file.read()

# Mengenkripsi konten file
encrypted = fernet.encrypt(original)

# Menyimpan hasil enkripsi ke file baru
with open('fileterenkripsi.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

