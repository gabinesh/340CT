import sqlite3 as db

def loadTrend(code):
    """function which gets trend status according to item code inputted"""
    connect = db.connect('SCM_DATABASE.db')
    connect.row_factory = lambda cursor, row: row[0]
    database = connect.cursor()

    trend = database.execute('SELECT salesTrend FROM sales WHERE code=?',(code,)).fetchall()
    return trend[0]#returns item codes sale trend


def loadStock():
    """function that loads each columns:values as lists where each list holds the values of one column in order"""
    connect = db.connect('SCM_DATABASE.db')
    connect.row_factory = lambda cursor, row: row[0]
    database = connect.cursor()
