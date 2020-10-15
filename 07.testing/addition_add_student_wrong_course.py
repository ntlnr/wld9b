import pytest
import System
import Student

def test_add_student_wrong_course():
    DB = System.System()
    DB.load_data()
    DB.login('calyam', '#yeet')
    DB.usr.add_student('akend3', 'software_engineering')
    DB.reload_data()
    DB.login('akend3', '123454321')
    assert 'software_engineering' not in DB.usr.courses