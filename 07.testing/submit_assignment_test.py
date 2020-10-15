import System
import Student

def test_submit_assignment():
    DB = System.System()
    DB.login('hdjsr7', 'pass1234')
    DB.usr.submit_assignment('cloud_computing', 'assignment3', 'this is a submission', '03/29/20')
    data = DB.load_user_db()
    assert data['hdjsr7']['courses']['cloud_computing']['assignment3']['ontime'] == True