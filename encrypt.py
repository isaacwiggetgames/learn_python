import nacl.secret
import nacl.utils
import os

# Generate a random key for encryption
key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)

# Create the encryption box with the generated key
box = nacl.secret.SecretBox(key)

# Save the key to secret.key
with open('secret.key', 'wb') as key_file:
    key_file.write(key)

# Get all files in the directory
all_files = os.listdir()
print("All files in directory:", all_files)

# List all files in the current directory, excluding encrypt.py, decrypt.py, and secret.key
files_to_encrypt = [f for f in all_files if f not in ['encrypt.py', 'decrypt.py', 'secret.key', 'manual_decrypt.py']]

print("Files selected for encryption:", files_to_encrypt)

if not files_to_encrypt:
    print("No files found to encrypt.")
else:
    # Encrypt each file
    for file_path in files_to_encrypt:
        try:
            # Open the file and read the content
            with open(file_path, 'rb') as f:
                file_data = f.read()

            # Encrypt the data
            encrypted_data = box.encrypt(file_data)

            # Overwrite the original file with the encrypted data
            with open(file_path, 'wb') as f:
                f.write(encrypted_data)

            print(f"File {file_path} has been encrypted.")

        except Exception as e:
            print(f"Error during encryption of {file_path}: {e}")

print("Encryption completed for all selected files.")
