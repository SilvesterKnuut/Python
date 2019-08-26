# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:17:38 2019

@author: Silvester
"""

from tkinter import *
import book_store_backend

def get_sellected_row(event):
    index=list_box.curselection()[0]
    print(index)
      
def view_in_listbox():
    list_box.delete(0.0,END)# empty the list, wont allow adding more rows if view is clicked multiple times 
    for row in book_store_backend.view_all():
        list_box.insert(END, row)# "END" inserts a new row at the end of the existing rows
        print(row)
        
def search_command():
    list_box.delete(0.0,END)
    for row in book_store_backend.search(ent_title.get(),ent_author.get(),ent_year.get(),ent_isbn.get()):
        list_box.insert(END, row)
        
def add_entry():
    book_store_backend.add(ent_title.get(),ent_author.get(),ent_year.get(),ent_isbn.get())
    list_box.delete(0.0,END)
    list_box.insert(END, (ent_title.get(),ent_author.get(),ent_year.get(),ent_isbn.get()))
        
window_main = Tk()
window_main.wm_title("Book Store BETA")

l_title = Label(window_main,text="Title",anchor=CENTER)
l_title.grid(row=0,column=0)

l_year = Label(window_main,text="Year",anchor=CENTER)
l_year.grid(row=1,column=0)

l_author = Label(window_main,text="Author",anchor=CENTER)
l_author.grid(row=0,column=2)

l_isbn = Label(window_main,text="ISBN",anchor=CENTER)
l_isbn.grid(row=1,column=2)

ent_title=StringVar()
ent_title=Entry(window_main,textvariable=ent_title)
ent_title.grid(row=0,column=1)

ent_author=StringVar()
ent_author=Entry(window_main,textvariable=ent_author)
ent_author.grid(row=0,column=3)

ent_year=StringVar()
ent_year=Entry(window_main,textvariable=ent_year)
ent_year.grid(row=1,column=1)

ent_isbn=StringVar()
ent_isbn=Entry(window_main,textvariable=ent_isbn)
ent_isbn.grid(row=1,column=3)

btn_view_all=Button(window_main,text="View All", width=12, command = view_in_listbox)
btn_view_all.grid(row=2,column=3)

btn_search=Button(window_main,text="Search", width=12, command = search_command)
btn_search.grid(row=3,column=3)

btn_add=Button(window_main,text="Add", width=12, command = add_entry)
btn_add.grid(row=4,column=3)

btn_update=Button(window_main,text="Update", width=12)
btn_update.grid(row=5,column=3)

btn_delete=Button(window_main,text="Delete", width=12)
btn_delete.grid(row=6,column=3)

btn_close=Button(window_main,text="Close", width=12)
btn_close.grid(row=7,column=3)

list_box=Text(window_main,height=6,width=35)
list_box.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll_bar=Scrollbar(window_main)
scroll_bar.grid(row=2, column=2, rowspan=6)

list_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_box.yview)

list_box.bind('<<ListboxSellect>>', get_sellected_row)

window_main.mainloop()