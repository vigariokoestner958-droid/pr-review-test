import sqlite3, time

def transfer(from_id, to_id, amount):
    conn = sqlite3.connect("bank.db")
    bal = conn.execute("SELECT balance FROM accounts WHERE id=?", (from_id,)).fetchone()[0]
    if bal < amount:
        return False
    time.sleep(0.01)   # 模拟延迟，竞态窗口
    conn.execute("UPDATE accounts SET balance=balance-? WHERE id=?", (amount, from_id))
    conn.execute("UPDATE accounts SET balance=balance+? WHERE id=?", (amount, to_id))
    conn.commit()
    return True
