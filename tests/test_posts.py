import datetime
from lib.posts import Post
from lib.post_repository import PostRepository

def test_create_post():

    new_post = Post(None, "This is a new post by anonymous", 1, '2023-10-01')
    assert new_post.message == "This is a new post by anonymous"
    assert new_post.user_id == 1

def test_list_all_posts(db_connection):

    db_connection.seed('seeds/post.sql')
    repository = PostRepository(db_connection)

    new_post_1 = Post(None, "This is a new post by anonymous", 1, '2023-10-01')
    repository.add_post(new_post_1.message, new_post_1.user_id)

    assert len(repository.get_all_posts()) == 3
    
    #INSERT INTO posts (content, user_id) VALUES ('This is a post', 1);

#This test was used for debugging purposes
def test_post_full(db_connection):
    db_connection.seed('seeds/post.sql')
    repository = PostRepository(db_connection)

    new_post_1 = Post(None, "This is a new post by anonymous", 1, '2023-10-01')
    repository.add_post(new_post_1.message, new_post_1.user_id)
    post_with_author = repository.get_post_by_id(1)
    assert post_with_author.user_id == 1
