import sqlite3
import os

def init_db():
    conn = sqlite3.connect('app.db')
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,  -- stored as plaintext
            email TEXT,
            is_admin INTEGER DEFAULT 0
        )
    """)
    # Default admin with hardcoded password
    conn.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', 'admin123', 'admin@app.com', 1)")
    conn.commit()

def find_user(username, password):
    conn = sqlite3.connect('app.db')
    # SQL injection + plaintext password comparison
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    return conn.execute(query).fetchone()

def update_user_email(user_id, new_email):
    conn = sqlite3.connect('app.db')
    # No ownership check - any user can update any email
    conn.execute(f"UPDATE users SET email='{new_email}' WHERE id={user_id}")
    conn.commit()
    return True

def get_user_by_email(email):
    conn = sqlite3.connect('app.db')
    # Returns full row including password
    return conn.execute(f"SELECT * FROM users WHERE email='{email}'").fetchone()

def delete_user(user_id):
    conn = sqlite3.connect('app.db')
    # No auth check, no soft delete
    conn.execute(f"DELETE FROM users WHERE id={user_id}")
    conn.commit()
    print(f"Deleted user {user_id}")
