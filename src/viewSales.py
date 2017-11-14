import sqlite3 as db

def loadTrend():
    """function which gets trend status according to item code inputted"""
    connect = db.connect('SCM_DATABASE.db')
    connect.row_factory = lambda cursor, row: row[0]
    database = connect.cursor()

