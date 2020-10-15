import pytest
import System
import User
import TA
import Student
import Staff

def test_change_wrongstaff_grade():
    database = System.System()
    database.login('cmhbf5', 'bestTA')
    database.usr.change_grade('hdjsr7', 'databases', 'assignment1', 10)
    database.reload_data()
    database.login('hdjsr7', 'pass1234')
    database.reload_data()
    grades = database.usr.check_grades('databases')
    assert grades[0] == ['assignemnt1', 10]