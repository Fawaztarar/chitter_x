import datetime
import psycopg2
from lib.posts import Post
from lib.database_connection import DatabaseConnection

class PostRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_post_by_id(self, post_id):
        post_data = self.db_connection.execute("SELECT * FROM posts WHERE id = %s", (post_id,))
        if post_data:
            post_data = post_data[0]
            return Post(post_data['id'], post_data['message'], post_data['user_id'], post_data['timestamp'])
        return None

    def add_post(self, content, user_id):
        cursor  = self.db_connection.execute(
        'INSERT INTO posts (message, user_id) VALUES (%s, %s) RETURNING id',
        [content, user_id])
        return cursor[0]['id']

    # Additional methods like update_post, delete_post, etc., can be defined here as needed.

    def get_all_posts(self):
        post_data = self.db_connection.execute("SELECT * FROM posts")
        posts = []
        for data in post_data:
            print(data)
            posts.append(Post(data["id"], data["message"], data["user_id"], data["timestamp"]))
        return posts
        
    def delete_post(self, post_id):
        self.db_connection.execute("DELETE FROM posts WHERE id = %s", [post_id])
        return None
        
    def update_post(self, post: Post):
        # timestamp_str = datetime.utcfromtimestamp(post.timestamp).strftime('%Y-%m-%d %H:%M:%S')
        self.db_connection.execute("UPDATE posts SET message = %s, user_id = %s, timestamp = to_timestamp(%s) WHERE id = %s", (post.message, post.user_id, post.timestamp, post.id))
        return None
        
    def get_posts_by_user_id(self, user_id):
        lst = []
        posts = self.db_connection.execute("SELECT * FROM posts WHERE user_id = %s", (user_id,))
        if posts:
            for data in posts:
                lst.append(Post(data["id"], data["message"], data["user_id"], data["timestamp"]))
            return lst
        return None
        