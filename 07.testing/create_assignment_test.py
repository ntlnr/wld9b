import pytest
import System


def test_create_assignment():
    DB = System.System()
    DB.login('cmhbf5', 'bestTA')
    DB.load_data()
    DB.usr.create_assignment('assignment3', '10/14/20', 'cloud_computing')
    data = DB.load_course_db()
    assert data['cloud_computing']['assignments']['assignment3']['due_date'] == '10/14/20'