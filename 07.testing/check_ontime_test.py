import System

def test_check_ontime():
    database = System.System()
    database.login('hdjsr7', 'pass1234')
    database.usr.submit_assignment('cloud_computing', 'assignment2', 'resubmit', '03/10/20')
    data = database.load_user_db()
    assert data['hdjsr7']['courses']['cloud_computing']['assignment2']['ontime'] == False