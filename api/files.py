import os
from flask import Flask, send_file, request, abort

app = Flask(__name__)
UPLOAD_DIR = "/var/app/uploads"

@app.route("/download")
def download():
    name = request.args.get("file", "")
    path = os.path.join(UPLOAD_DIR, name)   # 未规范化路径
    if not os.path.exists(path):
        abort(404)
    return send_file(path)
