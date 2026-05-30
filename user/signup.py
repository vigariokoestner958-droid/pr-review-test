import sqlite3

def signup(username, password, email):
    conn = sqlite3.connect("users.db")
    conn.execute(
        "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
        (username, password, email)   # 密码明文存储
    )
    conn.commit()
    print(f"[DEBUG] New user: {username} pass={password}")
