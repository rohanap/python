import hashlib

# Define a message to hash
message = b"Hello, world!"

# Hash the message using the SHA-256 algorithm
hashed_message = hashlib.sha256(message)

# Print the original message and the hashed message
print("Original message:", message.decode())
print("Hashed message:", hashed_message.hexdigest())

