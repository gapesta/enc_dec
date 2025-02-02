#!/bin/bash

echo "Pilih opsi:"
echo "1) Encrypt File"
echo "2) Decrypt File"
read -p "Masukkan pilihan (1/2/3): " choice

case $choice in
    1)
        read -p "Masukkan nama file yang ingin dienkripsi: " file
        if [[ ! -f "$file" ]]; then
            echo "File tidak ditemukan!"
            exit 1
        fi
        read -sp "Masukkan password untuk enkripsi: " password
        echo
        openssl enc -aes-256-cbc -salt -in "$file" -out "$file.enc" -pass pass:"$password"
        echo "File berhasil dienkripsi: $file.enc"
        ;;
    2)
        read -p "Masukkan nama file yang ingin didekripsi: " file
        if [[ ! -f "$file" ]]; then
            echo "File tidak ditemukan!"
            exit 1
        fi
        read -sp "Masukkan password untuk dekripsi: " password
        echo
        openssl enc -d -aes-256-cbc -in "$file" -out "${file%.enc}" -pass pass:"$password"
        echo "File berhasil didekripsi: ${file%.enc}"
        ;;
    *)

        echo "Pilihan tidak valid!"
        exit 1
        ;;
esac
