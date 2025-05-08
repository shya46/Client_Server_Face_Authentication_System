import sqlite3

def delete_user(username):
    conn = sqlite3.connect("face_auth.db")  # Connect to the database
    cursor = conn.cursor()

    # Execute delete query
    cursor.execute("DELETE FROM users WHERE username = ?", (username,))
    
    # Commit and close connection
    conn.commit()
    conn.close()

    print(f"User '{username}' deleted successfully!")

# Example usage
user_to_delete = input("Enter username to delete: ")
delete_user(user_to_delete)
