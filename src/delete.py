import sqlite3 as db #loads sqlite python module


def prompt(code):
    """function that takes user input item code to generate and return
       item details for notification purposes"""
    
    connect = db.connect('SCM_DATABASE.db')
    connect.row_factory = lambda cursor, row: row[0]
    database = connect.cursor()

    codeReturn = database.execute('SELECT code FROM stock WHERE code =?',(code,)).fetchall()
    nameReturn = database.execute('SELECT name FROM stock WHERE code =?',(code,)).fetchall()
    quantityReturn = database.execute('SELECT quantity FROM stock WHERE code =?',(code,)).fetchall()

    
    return[codeReturn[0],nameReturn[0],quantityReturn[0]]#details for notification purposes


