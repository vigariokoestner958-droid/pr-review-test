import sqlite3

def search_users(keyword):
    conn = sqlite3.connect("users.db")
    sql = "SELECT id, username, email FROM users WHERE username LIKE '%" + keyword + "%'"
    return conn.execute(sql).fetchall()
