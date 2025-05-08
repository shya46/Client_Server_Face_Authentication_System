import socket
import cv2
import face_recognition
import pickle

SERVER_IP = "192.168.27.147"
PORT = 9999


video = cv2.VideoCapture(0)
ret, frame = video.read()
video.release()

if not ret:
    print("❌ Failed to capture frame")
    exit()

rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
encodings = face_recognition.face_encodings(rgb)

if not encodings:
    print("❌ No face detected")
    exit()

encoding = encodings[0]
data = pickle.dumps(encoding)

# Connect to server and send encoding
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))
client_socket.sendall(data)

# Receive response
response = client_socket.recv(1024)
print(response.decode())

client_socket.close()
