# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 16:17:38 2019

@author: Silvester
"""

import tkinter as tk
import book_store_backend_networked

def get_selected_row(event):
    try:
        global selected_tuple
        index=list_box.curselection()[0]
        selected_tuple=list_box.get(index)
        #print(index)
        #print(selected_tuple[3])
        #return(selected_tuple) no need to return selected_tuple, its a global variable and we can point to it
        ent_title.delete(0,tk.END)
        ent_title.insert(tk.END,selected_tuple[1])
        ent_author.delete(0,tk.END)
        ent_author.insert(tk.END,selected_tuple[2])
        ent_year.delete(0,tk.END)
        ent_year.insert(tk.END,selected_tuple[3])
        ent_isbn.delete(0,tk.END)
        ent_isbn.insert(tk.END,selected_tuple[4])
    except IndexError:
        pass
      
def view_in_listbox():
    list_box.delete(0,tk.END)#empty the list, wont allow adding more rows if view is clicked multiple times 
    for row in book_store_backend_networked.view_all():
        list_box.insert(tk.END, row)# "END" inserts a new row at the end of the existing rows
        #print(row)
        
def search_command():
    list_box.delete(0,tk.END)
    for row in book_store_backend_networked.search(ent_title.get(),ent_author.get(),ent_year.get(),ent_isbn.get()):
        list_box.insert(tk.END, row)
        
def add_entry():
    book_store_backend_networked.add(ent_title.get(),ent_author.get(),ent_year.get(),ent_isbn.get())
    list_box.delete(0,tk.END)
    list_box.insert(tk.END, (ent_title.get(),ent_author.get(),ent_year.get(),ent_isbn.get()))
    view_in_listbox()
    
def delete_command():
    book_store_backend_networked.delete(selected_tuple[0])
    #print(selected_tuple)
    #print(selected_tuple[0])
    view_in_listbox()
    
def update_command():
    book_store_backend_networked.update(selected_tuple[0],ent_title.get(),ent_author.get(),ent_year.get(),ent_isbn.get())
    view_in_listbox()
        
window_main = tk.Tk()
window_main.wm_title("Book Store NetDB 3.0")

l_title = tk.Label(window_main,text="Title",anchor=tk.CENTER)
l_title.grid(row=0,column=0)

l_year = tk.Label(window_main,text="Year",anchor=tk.CENTER)
l_year.grid(row=1,column=0)

l_author = tk.Label(window_main,text="Author",anchor=tk.CENTER)
l_author.grid(row=0,column=2)

l_isbn = tk.Label(window_main,text="ISBN",anchor=tk.CENTER)
l_isbn.grid(row=1,column=2)

ent_title=tk.StringVar()
ent_title=tk.Entry(window_main,textvariable=ent_title)
ent_title.grid(row=0,column=1)

ent_author=tk.StringVar()
ent_author=tk.Entry(window_main,textvariable=ent_author)
ent_author.grid(row=0,column=3)

ent_year=tk.StringVar()
ent_year=tk.Entry(window_main,textvariable=ent_year)
ent_year.grid(row=1,column=1)

ent_isbn=tk.StringVar()
ent_isbn=tk.Entry(window_main,textvariable=ent_isbn)
ent_isbn.grid(row=1,column=3)

btn_view_all=tk.Button(window_main,text="View All", width=12, command = view_in_listbox)
btn_view_all.grid(row=2,column=3)

btn_search=tk.Button(window_main,text="Search", width=12, command = search_command)
btn_search.grid(row=3,column=3)

btn_add=tk.Button(window_main,text="Add", width=12, command = add_entry)
btn_add.grid(row=4,column=3)

btn_update=tk.Button(window_main,text="Update", width=12, command = update_command)
btn_update.grid(row=5,column=3)

btn_delete=tk.Button(window_main,text="Delete", width=12, command = delete_command)
btn_delete.grid(row=6,column=3)

btn_close=tk.Button(window_main,text="Close", width=12, command = window_main.destroy)
btn_close.grid(row=7,column=3)

list_box=tk.Listbox(window_main,height=6,width=35)
list_box.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll_bar=tk.Scrollbar(window_main)
scroll_bar.grid(row=2, column=2, rowspan=6)

list_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_box.yview)

list_box.bind('<<ListboxSelect>>', get_selected_row)

window_main.mainloop()