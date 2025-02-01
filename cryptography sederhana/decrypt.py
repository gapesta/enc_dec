from cryptography.fernet import Fernet

# Memuat kunci dari file
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

# Inisialisasi objek Fernet dengan kunci
fernet = Fernet(key)
# Membaca file terenkripsi
with open('fileterenkripsi.txt', 'rb') as enc_file:
    encrypted = enc_file.read()

# Mendekripsi konten file
decrypted = fernet.decrypt(encrypted)

# Menyimpan hasil dekripsi ke file baru
with open('filedekripsi.txt', 'wb') as dec_file:
    dec_file.write(decrypted)
