from lib.users import User
from lib.users_repository import UserRepository
import pytest


def test_user_find_by_email(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)

    tom = User(None, "Tom", "TomMazzag", "tom@mazzag.com", "testPassw0rd")
    repository.create(tom.name, tom.username, tom.email, tom.password)

    result = repository.find_user(tom.email, tom.password)
    print(result)
    assert result['email'] == tom.email

def test_user_find_by_username(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)

    tom = User(None, "Tom", "TomMazzag", "tom@mazzag.com", "testPassw0rd")
    repository.create(tom.name, tom.username, tom.email, tom.password)

    result = repository.find_user(tom.email, tom.password)
    print(result)
    assert result != None