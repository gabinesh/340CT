import sqlite3 as db



def refundItem(search,typ):
    """"function that recieves details from the user input regarding refund and returns the correct details
         for the refund according to whether the user selects item code or item name"""
    
    connect = db.connect('SCM_DATABASE.db')
    connect.row_factory = lambda cursor, row: row[0]
    database = connect.cursor()
    
    if typ == "code":#returns details if item code is primary method of item refund
        code1 = database.execute('SELECT code FROM stock WHERE code=?',(search,)).fetchall()
        code = code1[0]
        name1 = database.execute('SELECT name FROM stock WHERE code=?',(search,)).fetchall()
        name = name1[0]
        price1 = database.execute('SELECT price FROM stock WHERE code=?',(search,)).fetchall()
        price = price1[0]
        quantity1 = database.execute('SELECT quantity FROM stock WHERE code=?',(search,)).fetchall()
        quantity = quantity1[0]

        return[code,name,price,quantity]#details sent back to gui for notification message




    
