import pytest
import System
import Student

def test_drop_student_wrong_course():
    DB = System.System()
    DB.load_data()
    DB.login('goggins', 'augurrox')
    DB.usr.drop_student('akend3', 'cloud_computing')
    DB.reload_data()
    checking = DB.load_user_db()
    assert checking['akend3']['courses'] == 'cloud_computing'