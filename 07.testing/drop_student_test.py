import System
import Professor

def test_drop_student():
    DB = System.System()
    DB.load_data()
    DB.login('saab', 'boomr345')
    DB.usr.drop_student('akend3', 'comp_sci')
    DB.reload_data()
    checking = DB.load_user_db()
    assert checking['akend3']['courses'] != 'comp_sci'