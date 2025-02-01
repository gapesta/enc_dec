import cryptographi


def main():
    encryptor = cryptographi.FileEncryptor()

    while True:
        print("\nMenu:")
        print("1. Create Key")
        print("2. Delete Key")
        print("3. Encrypt File")
        print("4. Encrypt Folder")
        print("5. Decrypt File")
        print("6. Decrypt Folder")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ").strip()
        
        if choice == "1":
            encryptor.create_key()
        elif choice == "2":
            encryptor.delete_key()
        elif choice == "3":
            file_path = input("Enter the file path to encrypt: ").strip()
            output_path = input("Enter the output file path (optional): ").strip()
            encryptor.encrypt_file(file_path, output_path or None)
        elif choice == "4":
            folder_path = input("Enter the folder path to encrypt: ").strip()
            output_folder = input("Enter the output folder path (optional): ").strip()
            encryptor.encrypt_folder(folder_path, output_folder or None)
        elif choice == "5":
            file_path = input("Enter the file path to decrypt: ").strip()
            output_path = input("Enter the output file path (optional): ").strip()
            encryptor.decrypt_file(file_path, output_path or None)
        elif choice == "6":
            folder_path = input("Enter the folder path to decrypt: ").strip()
            output_folder = input("Enter the output folder path (optional): ").strip()
            encryptor.decrypt_folder(folder_path, output_folder or None)
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
