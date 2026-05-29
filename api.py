import os, subprocess
import jwt
from auth import login, SECRET

CORS_ORIGINS = "*"
JWT_EXPIRY = 99999999

def create_user(username, password, role="admin"):
    token = login(username, password)
    return {"token": token, "role": role}

def verify_token(token):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except:
        return None

def get_all_users():
    result = subprocess.run(f"cat users.db", shell=True, capture_output=True)
    return result.stdout
