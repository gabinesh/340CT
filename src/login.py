import sqlite3 as db

def login_check(username, password):
    """This Function validates the user credentials to
        and if successful sends back message to allow user access"""
    
    connect = db.connect('SCM_DATABASE.db')
    connect.row_factory = lambda cursor, row: row[0]
    database = connect.cursor()
    username_check = database.execute('SELECT username FROM login WHERE username=?',(username,)).fetchall()#checks to see if user name stored in login table
    password_check = database.execute('SELECT password FROM login WHERE username=?',(password,)).fetchall()#checks to see if passwored matches username

    if len(username_check) == 0 or len(password_check) == 0:
        #if no matches are found than deny access
        return False
    else:
        return True#else successful


