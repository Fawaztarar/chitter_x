import os
from lib.database_connection import get_flask_database_connection
from flask import Flask, request, render_template, redirect, url_for
from lib.users import User
from lib.users_repository import UserRepository
from lib.posts import Post
from lib.post_repository import PostRepository
from datetime import datetime
import psycopg2 as psycopg




def get_database_url():
    # The app can run in two 'modes' — production mode, or development mode.
    # This is determined by the `APP_ENV` environment variable.
    # Having dev and production modes is quite a common pattern and you will
    # see it in many real-world applications.
    if os.environ.get("APP_ENV") == "PRODUCTION":
        password = os.environ.get("POSTGRES_PASSWORD")
        hostname = os.environ.get("POSTGRES_HOSTNAME")
        # This URL below is constructed out of the password and hostname
        # We'll use this URL to connect to the database in production
        return f"postgres://postgres:{password}@{hostname}:5432/postgres"
    else:
        # This URL is for our local database. You may need to edit it.
        return "postgres://localhost:5432/postgres"

# We're going to write a function that sets up the database with the right table
def setup_database(url):
    # We connect using the URL
    connection = psycopg.connect(url)

    # Get a 'cursor' object that we can use to run SQL
    cursor = connection.cursor()

    # Execute some SQL to create the table
    cursor.execute("CREATE TABLE IF NOT EXISTS messages (message TEXT);")

    # And commit the changes to ensure that they 'stick' in the database.
    connection.commit()

# We run the two functions above
POSTGRES_URL = get_database_url()
setup_database(POSTGRES_URL)










# Create a new Flask app
app = Flask(__name__)
app.jinja_env.autoescape = True
login_id = 3
# == Your Routes Here ==

@app.route('/chitter')
def get_menu():
    connection = get_flask_database_connection()
    post_repo = PostRepository(connection)
    posts = post_repo.get_all_posts()
    return render_template('/chitter/index.html', posts = posts, login_id = login_id)

@app.route('/chitter/post/new')
def new_post():
    return render_template('/chitter/new_post.html', login_id = login_id)

@app.route('/chitter', methods = ['POST'])
def add_new_post():
    connection = get_flask_database_connection()
    repo = PostRepository(connection)
    content = request.form['content']
    user_id = request.form['user_id']
    # print(content, user_id)
    repo.add_post(content, user_id)
    return redirect('/chitter')


@app.route('/chitter/login')
def user_login():
    return render_template('/chitter/login.html')

@app.route('/chitter/login', methods=['POST'])
def login_user():
    connection = get_flask_database_connection()
    repo = UserRepository(connection)
    user = request.form['email']
    password = request.form['password']
    print(user, password)
    # Authenticate user
    authenticated_user = repo.verify_password(user, password)
    # print(authenticated_user)
    if authenticated_user:
        login_id = authenticated_user["id"]
        # print(login_id)
        # Authentication successful, redirect to the main page
        return redirect('/chitter')
    else:
        # Authentication failed, render the login page with an error message
        return render_template('/chitter/login.html', error='Invalid username or password')


@app.route('/chitter/signup')
def user_signup():
    return render_template('/chitter/signup.html')

@app.route('/chitter/signup', methods=['POST'])
def add_user():
    connection = get_flask_database_connection()
    repo = UserRepository(connection)
    name = request.form['name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    repo.create(name, username, email, password)
    # print(repo.all())
    # Redirect after successfully adding the user
    return redirect('/chitter')

@app.route('/chitter/user/<user_id>')
def get_user(user_id):
    connection = get_flask_database_connection()
    repo = UserRepository(connection)
    # print(repo.all())
    user = repo.get_user_by_id(user_id)
    return render_template('/chitter/user.html', user = user)

@app.route('/chitter/user/<user_id>/edit')
def edit_user(user_id):
    connection = get_flask_database_connection()
    repo = UserRepository(connection)
    user = repo.get_user_by_id(user_id)
    return render_template('/chitter/edit_user.html', user = user)

@app.route('/chitter/user/<user_id>/edit', methods = ['POST'])
def update_user(user_id):
    connection = get_flask_database_connection()
    repo = UserRepository(connection)
    name = request.form['name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    user = User(user_id,
                name,
                username,
                password,
                email)
    repo.update_user(user)
    return redirect('/chitter/user/' + user_id)

@app.route('/chitter/user/<user_id>/delete')
def delete_user(user_id):
    connection = get_flask_database_connection()
    repo = UserRepository(connection)
    repo.delete(user_id)
    return redirect('/chitter')

@app.route('/chitter/post/<post_id>')
def get_post(post_id):
    connection = get_flask_database_connection()
    repo = PostRepository(connection)
    post = repo.get_post_by_id(post_id)
    return render_template('/chitter/post.html', post = post)


@app.route('/chitter/post/<post_id>/edit', methods = ['POST'])
def update_post(post_id):
    connection = get_flask_database_connection()
    repo = PostRepository(connection)
    message = request.form['content']
    post = Post(post_id,
                message, login_id,
                datetime.now().timestamp())
    print(post)
    repo.update_post(post)
    return redirect('/chitter')

@app.route('/chitter/post/<post_id>/delete')
def delete_post(post_id):
    connection = get_flask_database_connection()
    repo = PostRepository(connection)
    repo.delete_post(post_id)
    return redirect('/chitter')

# This route simply returns the login page
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/emoji', methods=['GET'])
def get_emoji():
    return render_template('emoji.html', emoji=':)')

if __name__ == '__main__':
    # Check if the application environment is set to production
    if os.environ.get("APP_ENV") == "PRODUCTION":
        # Run without debug mode in production
        app.run(port=int(os.environ.get('PORT', 5000)), host='0.0.0.0')
    else:
        # Run with debug mode in non-production environments
        app.run(debug=True, port=int(os.environ.get('PORT', 5000)), host='0.0.0.0')






















