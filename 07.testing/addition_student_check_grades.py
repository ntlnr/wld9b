import pytest
import System
import Student

def test_student_check_grades():
    DB = System.System()
    DB.login('hdjsr7', 'pass1234')
    checking = DB.usr.check_grades('hdjsr7', 'cloud_computing')
    assert checking == []