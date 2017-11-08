import sqlite3 as db

def login_check(username, password):
    """This Function validates the user credentials to
        and if successful sends back message to allow user access"""
    
    connect = db.connect('SCM_DATABASE.db')
    connect.row_factory = lambda cursor, row: row[0]
    database = connect.cursor()


