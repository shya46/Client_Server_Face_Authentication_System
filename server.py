import socket
import sqlite3
import pickle
import numpy as np
import face_recognition
from encryptor import decrypt_encoding, load_key

# Load the encryption key
key = load_key()

# Server configuration
HOST = '0.0.0.0'
PORT = 9999

# Load user data from SQLite and decrypt encodings
def load_users():
    conn = sqlite3.connect("face_auth.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, face_encoding FROM users")
    users = cursor.fetchall()
    conn.close()
    return [(u, decrypt_encoding(enc, key)) for u, enc in users]

# Face match helper
def is_match(known_encoding, test_encoding, tolerance=0.4):
    distance = face_recognition.face_distance([known_encoding], test_encoding)[0]
    return distance <= tolerance

# Start server
print("🔌 Server starting...")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"✅ Listening on {HOST}:{PORT}")

# Load all known users and encodings
users = load_users()
known_usernames = [u for u, _ in users]
known_encodings = [e for _, e in users]
print(f"📦 Loaded {len(users)} users from database.")

while True:
    client_socket, addr = server_socket.accept()
    print(f"\n📡 Connection from {addr}")

    data = b""
    while True:
        packet = client_socket.recv(4096)
        if not packet: break
        data += packet

    try:
        frame_encoding = pickle.loads(data)
        print("👤 Received face encoding. Authenticating...")

        for i, known in enumerate(known_encodings):
            if is_match(known, frame_encoding):
                response = f"✅ Access Granted! Welcome, {known_usernames[i]}"
                break
        else:
            response = "❌ Access Denied! Face not recognized."

    except Exception as e:
        response = f"❌ Error processing data: {str(e)}"

    print("📨 Sending response to client...")
    client_socket.send(response.encode('utf-8'))
    client_socket.close()
