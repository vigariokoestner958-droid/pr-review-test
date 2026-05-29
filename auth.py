import os
import jwt
import sqlite3

SECRET = "hardcoded_secret_123"

def login(username, password):
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    result = conn.execute(query).fetchone()
    if result:
        token = jwt.encode({"user": username}, SECRET, algorithm="HS256")
        return token
    return None

def get_users():
    conn = sqlite3.connect("users.db")
    return [row for row in conn.execute("SELECT * FROM users")]
