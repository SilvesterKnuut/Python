# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:00:54 2019

@author: Silvester

            Standart proces to interact with a db:
1. Connect to  a database
2. Create a cursor object (Its a pointer to access rows from the table of a db)
3. Apply an SQL query
4. Commit the changes to the database
5. Close the conection to the db

"""

import sqlite3

def create_table():
    DB_Connection = sqlite3.connect("StoreDB.db")
    CursorObj = DB_Connection.cursor()
    CursorObj.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    DB_Connection.commit()
    DB_Connection.close()
    
def insert(DB_item, quantity, price):
    DB_Connection = sqlite3.connect("StoreDB.db")
    CursorObj = DB_Connection.cursor()
    CursorObj.execute("INSERT INTO store VALUES(?,?,?)",(DB_item, quantity, price))
    DB_Connection.commit()
    DB_Connection.close()

def delete(DB_item):
    DB_Connection = sqlite3.connect("StoreDB.db")
    CursorObj = DB_Connection.cursor()
    CursorObj.execute("DELETE FROM store WHERE item=?",(DB_item,))# the "comma" after DB_item, is necessary
    DB_Connection.commit()
    DB_Connection.close()
    
def update(DB_item, quantity, price):
    DB_Connection = sqlite3.connect("StoreDB.db")
    CursorObj = DB_Connection.cursor()
    CursorObj.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity, price, DB_item))
    DB_Connection.commit()
    DB_Connection.close()

def viewDB():
    DB_Connection = sqlite3.connect("StoreDB.db")
    CursorObj = DB_Connection.cursor()
    CursorObj.execute("SELECT * FROM store")
    rows=CursorObj.fetchall()
    DB_Connection.close()
    return rows
    
create_table()
#insert("Orange juice",64,98)
update("Coffe cup",2,3.4)
#delete("Coffe cup")
print(viewDB())