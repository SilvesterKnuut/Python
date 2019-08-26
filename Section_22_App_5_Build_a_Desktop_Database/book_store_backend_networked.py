# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 13:44:24 2019

@author: Silvester
"""

import psycopg2

def create_table():
    db_connection = psycopg2.connect("dbname='storedb_postgresql' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursorObj = db_connection.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS books (id SERIAL PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    db_connection.commit()
    db_connection.close()
    
create_table()
    
def view_all():
    db_connection = psycopg2.connect("dbname='storedb_postgresql' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor_obj = db_connection.cursor()
    cursor_obj.execute("SELECT * FROM books")
    rows=cursor_obj.fetchall()
    db_connection.close()
    return rows

def search(title="", author="", year="", isbn=""):
    db_connection = psycopg2.connect("dbname='storedb_postgresql' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor_obj = db_connection.cursor()
    cursor_obj.execute("SELECT * FROM books WHERE title=%s OR author=%s OR year=%s OR isbn=%s",(title, author, year, isbn))
    rows=cursor_obj.fetchall()
    db_connection.close()
    return rows

def add(title, author, year, isbn):
    db_connection = psycopg2.connect("dbname='storedb_postgresql' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor_obj = db_connection.cursor()
    cursor_obj.execute("INSERT INTO books(title, author, year, isbn) VALUES (%s,%s,%s,%s)", (title, author, year, isbn))
    db_connection.commit()
    db_connection.close()
    
def update(id, title="", author="", year="", isbn=""):
    db_connection = psycopg2.connect("dbname='storedb_postgresql' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor_obj = db_connection.cursor()
    cursor_obj.execute("UPDATE books SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s ",(title, author, year, isbn, id))
    db_connection.commit()
    db_connection.close()
    
def delete(id):
    db_connection = psycopg2.connect("dbname='storedb_postgresql' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor_obj = db_connection.cursor()
    cursor_obj.execute("DELETE FROM books WHERE id=%s",(id,))
    db_connection.commit()
    db_connection.close()

print(search("Ocean","", "", ""))
#update(2, "Ocean", "John C", 1985, 65987)
#add("Moon","John D", 1985, 32154)
#print(view_all())