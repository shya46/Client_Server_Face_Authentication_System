import sqlite3

def view_users():
    conn = sqlite3.connect("face_auth.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM users")
    users = cursor.fetchall()
    conn.close()

    if users:
        print("👤 Registered Users:")
        for user in users:
            print(f"ID: {user[0]}, Username: {user[1]}")
    else:
        print("⚠️ No users found.")

if __name__ == "__main__":
    view_users()
