from cryptography.fernet import Fernet

# Generate a random key for encryption and decryption
key = Fernet.generate_key()

# Create a Fernet object with the key
fernet = Fernet(key)

# Define a message to encrypt
message = "Hello, world!".encode()

# Encrypt the message using the Fernet object
encrypted_message = fernet.encrypt(message)

# Decrypt the message using the Fernet object
decrypted_message = fernet.decrypt(encrypted_message)

# Print the original message and the decrypted message
print("Decrypted message:", decrypted_message.decode())
print("Original message:", message.decode())
print("Messgae without using encode method:", encrypted_message)

