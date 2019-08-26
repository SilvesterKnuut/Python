# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 12:40:55 2019

@author: Silvester
"""

import time
from datetime import datetime as dt

#back up located at C:\Users\Silvester\Desktop\Personal\Python\The_Python_Mega_Course\Section9_App3_WebSite_Blocker\Hosts\BackUp_host_file
temporary_hostFile_path=r"C:\Users\Silvester\Desktop\Personal\Python\The_Python_Mega_Course\Section9_App3_WebSite_Blocker\Hosts\hosts"
hostFile_path =r"C:\Windows\System32\drivers\etc\hosts" # "r" is indicating that the following string is a row
#   -or-
# hostFile_path ="C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect = "127.0.0.1"
blockedWebsite_list=["www.facebook.com","facebook.com","www.lichess.org","lichess.org"]

while True:
    time.sleep(3)
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        with open(temporary_hostFile_path, 'r+') as file: # "r+" means read and append if there was only r then only 4 lines would be writtent to the file
            content=file.read()
            file.seek(0,2)
            for website in blockedWebsite_list:
                if website in content:
                    pass #python will move on with the excution to the next line
                else:
                    file.write(redirect+"    "+website+"\n")
        print("Get Backh to work !!!")
    else:
        with open(temporary_hostFile_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                 if not any(website in line for website in blockedWebsite_list):
                     file.write(line)
            file.truncate()
        print("Drink hard!!!")

