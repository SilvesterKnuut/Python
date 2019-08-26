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

import psycopg2

def create_table():
    DB_Connection = psycopg2.connect("dbname='storedb_postgresql' user='postgres' password='postgres123' host='localhost' port='5432'")
    CursorObj = DB_Connection.cursor()
    CursorObj.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    DB_Connection.commit()
    DB_Connection.close()
    
def insert(DB_item, quantity, price):
    DB_Connection = psycopg2.connect("dbname='storedb_postgresql' user='postgres' password='postgres123' host='localhost' port='5432'")
    CursorObj = DB_Connection.cursor()
    #-- prone to sql injections -- CursorObj.execute("INSERT INTO store VALUES('%s','%s','%s')" % (DB_item, quantity, price))
    CursorObj.execute("INSERT INTO store VALUES (%s,%s,%s) ", (DB_item, quantity, price))
    DB_Connection.commit()
    DB_Connection.close()

def delete(DB_item):
    DB_Connection = psycopg2.connect("dbname='storedb_postgresql' user='postgres' password='postgres123' host='localhost' port='5432'")
    CursorObj = DB_Connection.cursor()
    CursorObj.execute("DELETE FROM store WHERE item=%s", (DB_item,))# the "comma" after DB_item, is necessary
    DB_Connection.commit()
    DB_Connection.close()
    
def update(DB_item, quantity, price):
    DB_Connection = psycopg2.connect("dbname='storedb_postgresql' user='postgres' password='postgres123' host='localhost' port='5432'")
    CursorObj = DB_Connection.cursor()
    CursorObj.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, DB_item))
    DB_Connection.commit()
    DB_Connection.close()

def viewDB():
    DB_Connection = psycopg2.connect("dbname='storedb_postgresql' user='postgres' password='postgres123' host='localhost' port='5432'")
    CursorObj = DB_Connection.cursor()
    CursorObj.execute("SELECT * FROM store")
    rows=CursorObj.fetchall()
    DB_Connection.close()
    return rows
    
#create_table()
#insert("Coffe cup",1,1.2)
#update("Orange juice",2,3.4)
#delete("Orange juice")
#print(viewDB())