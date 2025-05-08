from cryptography.fernet import Fernet
import numpy as np

# Load or generate encryption key
def load_key():
    """Loads the encryption key from file."""
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# Encrypt a NumPy array (face encoding)
def encrypt_encoding(encoding, key):
    """Encrypts a NumPy face encoding array."""
    cipher = Fernet(key)
    encoding_bytes = encoding.tobytes()
    encrypted = cipher.encrypt(encoding_bytes)
    return encrypted

# Decrypt to NumPy array
def decrypt_encoding(encrypted_encoding, key):
    """Decrypts an encrypted face encoding into a NumPy array."""
    cipher = Fernet(key)
    decrypted_bytes = cipher.decrypt(encrypted_encoding)
    return np.frombuffer(decrypted_bytes, dtype=np.float64)

# Optional: Generate a new key and save it (run this only once)
def generate_key():
    """Generates and saves a new encryption key."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("🔑 New encryption key generated and saved as secret.key")

# If you want to generate a key, uncomment and run this once
# generate_key()
