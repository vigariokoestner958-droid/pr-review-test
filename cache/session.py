import pickle, redis, base64

r = redis.Redis(host="localhost", port=6379, db=0)

def save_session(sid, data):
    r.setex(f"sess:{sid}", 3600, pickle.dumps(data))

def load_session(sid):
    raw = r.get(f"sess:{sid}")
    return pickle.loads(raw) if raw else None   # 反序列化Redis数据

def load_from_cookie(cookie):
    # 直接反序列化用户cookie — 可导致RCE
    return pickle.loads(base64.b64decode(cookie))
