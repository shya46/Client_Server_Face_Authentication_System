import cv2
import face_recognition
import sqlite3
import numpy as np
from cryptography.fernet import Fernet
from encryptor import decrypt_encoding

# Load encryption key
cipher = Fernet(open("secret.key", "rb").read())

def authenticate_user():
    print("🔍 Starting authentication process...")

    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        print("❌ Could not open webcam.")
        return

    print("📡 Accessing database...")
    conn = sqlite3.connect("face_auth.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, face_encoding FROM users")
    users = cursor.fetchall()
    conn.close()

    if not users:
        print("❌ No users found in the database.")
        return

    print(f"📦 Loaded {len(users)} users from database.")

    known_usernames = []
    known_encodings = []

    for username, encrypted_encoding in users:
        decrypted_bytes = cipher.decrypt(encrypted_encoding)
        decrypted_encoding = np.frombuffer(decrypted_bytes, dtype=np.float64)
        known_usernames.append(username)
        known_encodings.append(decrypted_encoding)

    print("🎥 Capturing a frame from the camera...")
    ret, frame = video_capture.read()
    video_capture.release()
    cv2.destroyAllWindows()

    if not ret:
        print("❌ Failed to read from camera.")
        return

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    print(f"👤 Faces detected: {len(face_encodings)}")

    if not face_encodings:
        print("❌ No face detected in the frame.")
        return

    unknown_encoding = face_encodings[0]

    print("🔍 Comparing with known faces...")
    matches = face_recognition.compare_faces(known_encodings, unknown_encoding, tolerance=0.6)

    if True in matches:
        matched_index = matches.index(True)
        print(f"✅ Access Granted! Welcome, {known_usernames[matched_index]}")
    else:
        print("❌ Access Denied! No match found.")

if __name__ == "__main__":
    authenticate_user()
