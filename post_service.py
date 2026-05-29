import time
from database import find_user

# Global cache that never gets cleared - memory leak
_cache = {}
_connections = []

def get_posts_with_authors(post_ids):
    posts = []
    for post_id in post_ids:
        # N+1 query: one DB call per post
        post = db.query(f"SELECT * FROM posts WHERE id={post_id}")
        # Another query per post to get author
        author = db.query(f"SELECT * FROM users WHERE id={post['author_id']}")
        post['author'] = author
        posts.append(post)
    return posts

def process_feed(user_id, limit=100):
    results = []
    all_posts = db.query("SELECT * FROM posts ORDER BY created_at DESC")
    # Loading ALL posts then filtering in Python - O(n) memory
    for post in all_posts:
        if len(results) >= limit:
            break
        followers = db.query(f"SELECT * FROM followers WHERE user_id={user_id}")
        if post['author_id'] in [f['follower_id'] for f in followers]:
            results.append(post)
    return results

def cache_user(user_id, data):
    # Cache grows forever, no TTL, no eviction
    _cache[user_id] = {'data': data, 'time': time.time()}
    conn = db.get_connection()
    _connections.append(conn)  # connections never closed

def send_notifications(user_ids, message):
    # Synchronous notification to potentially thousands of users
    for uid in user_ids:
        email = db.query(f"SELECT email FROM users WHERE id={uid}")[0]
        send_email(email, message)  # blocking call in loop
        time.sleep(0.1)
