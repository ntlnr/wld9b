import pytest
import System
import Student

def test_check_username():
    DB = System.System()
    DB.load_data()
    username = 'hdjsr7'
    password = 'pass12345'
    assert DB.check_password(username, password) == True