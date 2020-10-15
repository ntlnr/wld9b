import pytest
import System
import Student

def test_view_assignments():
    DB = System.System()
    DB.login('hdjsr7', 'pass1234')
    checking = DB.usr.view_assignments('databases')
    assert checking[0] == ['assignment1', '14/10/20']
    assert checking[1] == ['assignment2', '15/10/20']