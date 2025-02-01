import nacl.secret
import nacl.utils
import os

# Prompt the user to enter a password
password = input("Enter password to decrypt files: ")

# Check if the password is correct
if password != "12345":
    print("Incorrect password. Exiting.")
    exit()  # Exit the script if the password is incorrect

# Load the key from the secret.key file
with open('secret.key', 'rb') as key_file:
    key = key_file.read()

# Create the encryption box with the loaded key
box = nacl.secret.SecretBox(key)

# Get all files in the directory
all_files = os.listdir()
print("All files in directory:", all_files)

# List all encrypted files (any file that's been encrypted)
files_to_decrypt = [f for f in all_files if f not in ['encrypt.py', 'decrypt.py', 'secret.key']]

print("Files selected for decryption:", files_to_decrypt)

if not files_to_decrypt:
    print("No encrypted files found to decrypt.")
else:
    # Decrypt each file
    for file_path in files_to_decrypt:
        try:
            # Read the encrypted content of the file
            with open(file_path, 'rb') as f:
                encrypted_data = f.read()

            # Decrypt the data
            decrypted_data = box.decrypt(encrypted_data)

            # Overwrite the encrypted file with the decrypted data
            with open(file_path, 'wb') as f:
                f.write(decrypted_data)

            print(f"File {file_path} has been decrypted.")

        except Exception as e:
            print(f"Error during decryption of {file_path}: {e}")

# Delete secret.key after decryption
if os.path.exists('secret.key'):
    os.remove('secret.key')
    print("secret.key has been deleted.")

print("Decryption completed for all selected files and secret.key has been deleted.")
