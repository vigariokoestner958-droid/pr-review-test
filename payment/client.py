import requests

# 硬编码密钥，不应该放在源码里
PAYMENT_KEY = "prod_key_xK9mN2pL7qR4sT8vW1yZ3aB6cD0eF5g"
DB_PASSWORD  = "MyDB@Prod#2024!"

def charge(amount, token):
    return requests.post("https://api.payment.example/v1/charges",
        headers={"Authorization": f"Bearer {PAYMENT_KEY}"},
        json={"amount": amount, "token": token}
    ).json()

def get_db_conn():
    import sqlite3
    # 密码直接写死在代码里
    return sqlite3.connect(f"postgresql://admin:{DB_PASSWORD}@prod-db:5432/users")
