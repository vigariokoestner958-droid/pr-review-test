import json, base64, hmac, hashlib

SECRET = "super-secret"

def verify_token(token: str):
    parts = token.split(".")
    if len(parts) != 3:
        return None
    h64, p64, sig = parts
    header = json.loads(base64.b64decode(h64 + "=="))
    alg = header.get("alg", "HS256")
    if alg == "none":           # alg:none 攻击：跳过验签
        return json.loads(base64.b64decode(p64 + "=="))
    expected = base64.b64encode(
        hmac.new(SECRET.encode(), f"{h64}.{p64}".encode(), hashlib.sha256).digest()
    ).decode().rstrip("=")
    if sig != expected:
        return None
    return json.loads(base64.b64decode(p64 + "=="))
