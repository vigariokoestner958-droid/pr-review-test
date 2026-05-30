from models import Post, User

def get_feed():
    posts = Post.query.all()
    result = []
    for post in posts:
        author = User.query.get(post.author_id)   # N+1 查询
        result.append({
            "title": post.title,
            "author": author.username if author else "?",
        })
    return result
