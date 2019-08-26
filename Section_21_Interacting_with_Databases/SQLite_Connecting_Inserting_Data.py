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

DB_Connection = sqlite3.connect("MyFirstDB.db")
CursorObj = DB_Connection.cursor()
CursorObj.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
CursorObj.execute("INSERT INTO store VALUES ('Piggy', 8, 10.5)")
DB_Connection.commit()
DB_Connection.close()

def viewDB():
    DB_Connection = sqlite3.connect("MyFirstDB.db")
    CursorObj = DB_Connection.cursor()
    CursorObj.execute("SELECT * FROM store")
    rows=CursorObj.fetchall()
    DB_Connection.close()
    return rows
    
print(viewDB())