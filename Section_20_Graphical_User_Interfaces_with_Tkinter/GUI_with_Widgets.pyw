# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 10:45:15 2019

@author: Silvester
"""

from tkinter import *

window_main = Tk()

def converter():
    resultInGrams = float(EnterValue.get()) * 1000
    resultinPounds = float(EnterValue.get()) * 2.20462
    resultinOunces = float(EnterValue.get()) * 35.274
    TextBox1.delete(1.0,END)
    TextBox1.insert(END,str(resultInGrams)+" g")
    TextBox2.delete(1.0,END)
    TextBox2.insert(END,str(resultinPounds)+" lb")
    TextBox3.delete(1.0,END)
    TextBox3.insert(END,str(resultinOunces)+" oz")
    
text1 = Label(window_main,text="Kg",anchor=CENTER)
text1.grid(row=0,column=0)

EnterValue=StringVar()
EnterValue=Entry(window_main,textvariable=EnterValue)
EnterValue.grid(row=0,column=1)

btn1=Button(window_main,text="Convert",command=converter)
btn1.grid(row=0,column=2)

TextBox1=Text(window_main,height=1,width=20)
TextBox1.grid(row=1, column=0)

TextBox2=Text(window_main,height=1,width=20)
TextBox2.grid(row=1, column=1)

TextBox3=Text(window_main,height=1,width=20)
TextBox3.grid(row=1, column=2)

window_main.mainloop()