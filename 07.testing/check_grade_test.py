import System
import pytest

def test_check_grades():
    DB = System.System()
    DB.login('hdjsr7', 'pass1234')
    grades = DB.usr.check_grades('databases')
    assert grades[0] == ['assignment1', 100]
    assert  grades[1] == ['assignment2', 100]