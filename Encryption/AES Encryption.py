from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Define a message to encrypt
message = b"Hello, world!"

# Generate a new AES key
key = get_random_bytes(16)

# Create a new AES cipher object
cipher = AES.new(key, AES.MODE_EAX)

# Encrypt the message
ciphertext, tag = cipher.encrypt_and_digest(message)

# Print the encrypted message and tag
print("Encrypted message:", ciphertext.hex())
print("Tag:", tag.hex())

# Decrypt the message
cipher = AES.new(key, AES.MODE_EAX, cipher.nonce)
decrypted_message = cipher.decrypt_and_verify(ciphertext, tag)

# Print the original message and the decrypted message
print("Original message:", message.decode())
print("Decrypted message:", decrypted_message.decode())
