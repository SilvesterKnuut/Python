# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 12:03:19 2019

@author: Silvester
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def sk_home():
    #return "Website content goes here!"
    return render_template("home.html")

@app.route('/about/')
def sk_about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True) #Was getting  because running with debug=True is huge a security risk on servers that are exposed to the internet.
                         #If you're running the code on your local system then you should ignore that message. It's just a warning and there is no problem.
                         #If you are running your code on Heroku or a similar host service then you must be sure to run with debug=False.
