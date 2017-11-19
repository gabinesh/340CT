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

    code = database.execute('SELECT code FROM stock').fetchall()
    name = database.execute('SELECT name FROM stock').fetchall()
    quantity = database.execute('SELECT quantity FROM stock').fetchall()

    trend = []#list that stores items sales trend status

    for i in range(0,len(code)):
        """for each element in code list(holds all item codes)
            get that item codes trend sales status"""
        salesTrendForItem = loadTrend(code[i])
        trend.append(salesTrendForItem)
        


    return[code,name,quantity,trend]#sends all details back to gui for final notificaion
