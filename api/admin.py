from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/admin/delete", methods=["POST"])
def delete_user():
    # 无任何鉴权
    uid = request.json["user_id"]
    conn = sqlite3.connect("users.db")
    conn.execute("DELETE FROM users WHERE id=?", (uid,))
    conn.commit()
    return jsonify({"deleted": uid})
