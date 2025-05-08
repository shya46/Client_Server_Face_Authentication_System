# Client_Server_Face_Authentication_System

Overview:
This project implements a secure, real-time biometric authentication system using facial recognition. It uses machine learning to detect and authenticate users by analyzing their facial features. The system employs a client-server architecture where the client captures face data, encrypts it, and sends it to the server for authentication. The server compares the received face encoding with stored encodings and provides an authentication result.

Features:
1. Real-time face recognition with OpenCV and face_recognition.
2. Secure communication with encryption (Fernet).
3. Client-server architecture for modularity.
4. User registration by capturing and storing face data securely in SQLite.
5. Authentication accuracy based on face encoding comparison.

Installation & Requirements:
bash
Copy
Edit
pip install opencv-python face_recognition cryptography numpy
git clone https://github.com/your-repo/face-authentication-system.git
cd face-authentication-system

Usage:
Run server: python server.py
Run client: python client.py

How It Works:
Client captures face, extracts encoding, encrypts it, and sends to server.
Server compares the encoding to the database and returns authentication result.

Future Improvements:
Integrate multifactor authentication for enhanced security.
Develop a mobile app for real-time authentication.
Implement cloud-based authentication for scalability.

License:
MIT License

Contributing:
Pull requests are welcome! Report issues or contribute improvements.

Collaborators:

Shriya Jadhav - https://github.com/shya46
Arnav Jain - 

Contact:
For questions or collaboration, reach out to shriyajadhav46@gmail.com or open an issue in the GitHub repository.
