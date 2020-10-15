import pytest
import System
import User
import Student

def test_login_system():
    DB = System.System()
    DB.login('cmhbf5', 'bestTA')
    DB.load_data()
    user = DB.load_user_db()
    users = DB.usr
    assert users.name == "cmhbf5"
    assert users.password == 'bestTA'