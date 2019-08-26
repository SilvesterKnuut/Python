# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 10:43:20 2019

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
    db_connection = sqlite3.connect("Library.db")
    cursor_obj = db_connection.cursor()
    cursor_obj.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title STRING, author STRING, year INTEGER, isbn INTEGER)")#id is an auto-increment value, no need to pass it in any future function
    db_connection.commit()
    db_connection.close()
    
create_table()

def view_all():
    db_connection = sqlite3.connect("Library.db")
    cursor_obj = db_connection.cursor()
    cursor_obj.execute("SELECT * FROM books")
    rows=cursor_obj.fetchall()
    db_connection.close()
    return rows

def search(title="", author="", year="", isbn=""):# the ="" are neccessary for passing empty parameters by default if user enters only author
    db_connection = sqlite3.connect("Library.db")
    cursor_obj = db_connection.cursor()
    cursor_obj.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",(title, author, year, isbn))
    rows=cursor_obj.fetchall()
    db_connection.close()
    return rows

def add(title, author, year, isbn):
    db_connection = sqlite3.connect("Library.db")
    cursor_obj = db_connection.cursor()
    cursor_obj.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title, author, year, isbn))#NULL since id is an auto-increment value, no need to pass it in any future function
    db_connection.commit()
    db_connection.close()
    
def update(id, title="", author="", year="", isbn=""):
    db_connection = sqlite3.connect("Library.db")
    cursor_obj = db_connection.cursor()
    cursor_obj.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=? ",(title, author, year, isbn, id))
    db_connection.commit()
    db_connection.close()
    
def delete(id):
    db_connection = sqlite3.connect("Library.db")
    cursor_obj = db_connection.cursor()
    cursor_obj.execute("DELETE FROM books WHERE id=?",(id,))
    db_connection.commit()
    db_connection.close()

#print(search(author="Silvester Knuut"))
#add("Sun","John P", 2001, 962584)
#delete(4)
#update(3, title="Moon Moon",author="Shuruhin",year=2002,isbn=987456)
#print(view_all())