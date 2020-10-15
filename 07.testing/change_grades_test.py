import pytest
import System
import json
import User
import Staff



def test_change_grade():
    DB = System.System()
    DB.login('cmhbf5', 'bestTA')
    DB.usr.change_grade('hdjsr7', 'cloud_computing', 'assignment1', 60)
    DB.reload_data()
    DB.login('hdjsr7', 'pass1234')
    DB.reload_data()
    checking = DB.usr.check_grades('cloud_computing')
    assert checking[0] == ['assignemnt1', 60]