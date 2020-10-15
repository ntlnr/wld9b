import pytest
import System
import Professor
import Student


def test_add_student():
    DB = System.System()
    DB.load_data()
    DB.login('calyam', '#yeet')
    DB.usr.add_student('akend', 'databases')
    DB.reload_data()
    DB.login('akend3', '123454321')
    assert 'cloud_computing'  in DB.usr.courses