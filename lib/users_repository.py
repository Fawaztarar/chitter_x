from lib.database_connection import DatabaseConnection
from lib.users import User
import hashlib

class UserRepository:
    def __init__(self, connection):
        self._connection = connection


    def all(self):
        users = []
        rows = self._connection.execute("SELECT * FROM users")
        print(rows)
        for row in rows:
            user = User(row['id'], row["name"], row["username"], row["email"], str(row["password"]))
            users.append(user)
        return users
    
    def get_user_by_id(self,user_id):
        users = []
        rows = self._connection.execute("SELECT * FROM users WHERE id = %s", [user_id])
        for row in rows:
            user = User(row['id'], row["name"], row["username"], str(row["password"]),  row["email"])
            users.append(user)
        if users:
            return users[0]
        return None


    def create(self, email, password):
        # Hash the password
        binary_password = password.encode("utf-8")
        hashed_password = hashlib.sha256(binary_password).hexdigest()

        # Store the email and hashed password in the database
        self._connection.execute(
            'INSERT INTO users (email, password) VALUES (%s, %s)',
            [email, hashed_password])
        
        
    def create(self, name, username, email, password):
        # Hash the password
        # binary_password = password.encode("utf-8")
        # hashed_password = hashlib.sha256(binary_password).hexdigest()

        # Store the email and hashed password in the database
        self._connection.execute(
            'INSERT INTO users (name, username, password, email ) VALUES (%s, %s, %s, %s)',
            [name, username, password, email])

    def update_user(self, user: User):
        self._connection.execute(
            'UPDATE users SET name = %s, username = %s, password = %s, email = %s WHERE id = %s',
            [user.name, user.username, user.password, user.email, user.id])

    def find_user(self, email, password):
        # Find the user with the given email
        rows = self._connection.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s', [email, password])

        # If there is a user with that email, return it
        if rows:
            return rows[0]
        else: 
            return None
        

    def delete(self, user_id):
        self._connection.execute("DELETE FROM users WHERE id = %s", [user_id])
        return None

    def check_password(self, email, password_attempt):
        # Hash the password attempt
        binary_password_attempt = password_attempt.encode("utf-8")
        hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()

        # Check whether there is a user in the database with the given email
        # and a matching password hash, using a SELECT statement.
        rows = self._connection.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s',
            [email, hashed_password_attempt])
        
        # If that SELECT finds any rows, the password is correct.
        return len(rows) > 0
    
    def verify_password(self, email, password):
        return self.find_user(email, password)    