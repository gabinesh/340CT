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

    if typ == "name":#returns details if item name is primary method of item refund
        code1 = database.execute('SELECT code FROM stock WHERE name=?',(search,)).fetchall()
        code = code1[0]
        name1 = database.execute('SELECT name FROM stock WHERE name=?',(search,)).fetchall()
        name = name1[0]
        price1 = database.execute('SELECT price FROM stock WHERE name=?',(search,)).fetchall()
        price = price1[0]
        quantity1 = database.execute('SELECT quantity FROM stock WHERE name=?',(search,)).fetchall()
        quantity = quantity1[0]

        return[code,name,price,quantity]#details sent back to gui for notification message


def ReturnAndRefund(listForReturns):
    """function that carries out the returning/refunding of the item after user accepts are you
       sure notification"""
    
    name = listForReturns[0]
    price = listForReturns[1]
    reason = listForReturns[2]
    
    connect = db.connect('SCM_DATABASE.db')
    database = connect.cursor()

    database.execute('insert into returned values (NULL,?,?,?)' ,[name,price,reason])#inserts refunded item details into returned table
    connect.commit()

    returnNotification = "Item Returned: " + str(name)+ "\n"*2 + "Amount Returned to Customer: £" + str(price) + "\n" *4+ "REASON FOR RETURN: "+"\n"*2 + reason #creating final notifictaion details 
    
    return returnNotification #sending notification details back to user display box



    
