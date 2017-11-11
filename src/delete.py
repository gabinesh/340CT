import sqlite3 as db #loads sqlite python module


def prompt():
    """function that takes user input item code to generate and return
       item details for notification purposes"""
    
    connect = db.connect('SCM_DATABASE.db')
    connect.row_factory = lambda cursor, row: row[0]
    database = connect.cursor()

