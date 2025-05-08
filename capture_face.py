import cv2
import face_recognition
import sqlite3
import numpy as np
from cryptography.fernet import Fernet
from encryptor import load_key

# Load encryption key
cipher = Fernet(load_key())

def register_user(username):
    video_capture = cv2.VideoCapture(0)
    print("📷 Capturing face. Please look at the camera...")

    while True:
        ret, frame = video_capture.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)

        if face_locations:
            face_encoding = face_recognition.face_encodings(rgb_frame, face_locations)[0]
            
            # Print the face encoding before encryption
            print("\n🔢 Face Encoding (128-D Vector):")
            print(face_encoding)  # This prints the numerical face encoding
            
            encrypted_encoding = cipher.encrypt(face_encoding.tobytes())

            # Store in database
            conn = sqlite3.connect("face_auth.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, face_encoding) VALUES (?, ?)", (username, encrypted_encoding))
            conn.commit()
            conn.close()

            print(f"\n✅ User '{username}' registered successfully!")
            break

        cv2.imshow("Face Registration", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    username = input("Enter username: ")
    register_user(username)
