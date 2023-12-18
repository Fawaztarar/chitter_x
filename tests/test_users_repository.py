import pytest
from lib.users_repository import UserRepository
from lib.database_connection import DatabaseConnection
from lib.users import User

def test_user_find_by_id(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)

    user = repository.get_user_by_id(2)
    assert user is not None


def test_create_and_find_user(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)

    new_user = User(None, "Test User", "test_user", "test@example.com", "testPassword123")
    repository.create(new_user.name, new_user.username, new_user.email, new_user.password)

    result = repository.find_user(new_user.email, new_user.password)
    # print(result)
    assert result is not None
    assert result['name'] == new_user.name
    assert result['username'] == new_user.username
    assert result['email'] == new_user.email
    assert result['password'] == new_user.password

def test_update_user(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)

    user = repository.get_user_by_id(1)
    user.name = "Updated Name"
    user.username = "updated_username"
    user.email = "updated_email@example.com"
    user.password = "new_password"

    repository.update_user(user)

    updated_user = repository.get_user_by_id(1)

    assert updated_user is not None
    assert updated_user.name == "Updated Name"
    assert updated_user.username == "updated_username"
    assert updated_user.email == "updated_email@example.com"
    assert updated_user.password == "new_password"

def test_delete_user(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)

    # Assuming there is a user with id=1 in the test database
    user_to_delete = repository.get_user_by_id(1)

    repository.delete(user_to_delete.id)

    # Attempting to retrieve the deleted user should return None
    deleted_user = repository.get_user_by_id(1)

    assert deleted_user is None

def test_check_password(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)

    email = "alice.smith@example.com"
    correct_password = "hashed_password123"
    incorrect_password = "wrong_password"

    # Correct password check
    result_correct = repository.verify_password(email, correct_password)
    if (result_correct["password"] == correct_password):
        assert True
    

    # Incorrect password check
    result_incorrect = repository.verify_password(email, incorrect_password)
    if (result_incorrect == None):
        assert True
    
