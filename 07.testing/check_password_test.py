import pytest
import System
import Student

def test_check_password():
    DB = System.System()
    DB.load_data()
    username = 'cmhbf5'
    password = 'incorrectPassword'
    checking = DB.check_password(username, password)
    assert checking == False
    password = 1234567890
    checking = DB.check_password(username, password)
    assert checking == False
    password = 'potentialPassword'
    checking = DB.check_password(username, password)
    assert checking == False
    password = 'bestTA'
    checking = DB.check_password(username, password)
    assert checking == True