# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 12:36:07 2018

@author: Siddharth Goel
"""

import sqlite3
from datetime import datetime
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

sqlite_file = 'trial.db' #put the name of your sqlite file in single inverted commas
i=1

while True:
    if datetime.now().time().hour == 00: #change the number to present hour to see it working
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        tname = 'Entries_for_'+str(datetime.now().date().strftime('%d%m%Y'))
        c.execute('CREATE TABLE IF NOT EXISTS '+tname+' (ID TEXT PRIMARY KEY, Name TEXT, Time DATE, Status TEXT DEFAULT "Absent" )')
        c.execute('SELECT ID, Name FROM FaceBase')
        rows = c.fetchall()
        for row in rows:
            uid, name = row
            print(uid, name)
            values = (uid, name,)
            c.execute('INSERT INTO '+tname+' (ID, Name) VALUES(?, ?)', values)
        i += 1
        conn.commit()
        c.close()
        conn.close()    
        
    if datetime.now().time().hour == 01 and datetime.now().time().minute == 15: #change the number to present hour to see it working
        conn = sqlite3.connect(sqlite_file)
        tn='Entries_for_'+str(datetime.now().date().strftime('%d%m%Y'))
        c = conn.cursor()
        c.execute('SELECT * FROM '+tn)
        data = c.fetchall()
        print(data)
        df = pd.read_sql('SELECT * FROM '+tn, conn)
        writer = ExcelWriter(tn+'.xlsx')
        df.to_excel(writer,'Sheet1')
        writer.save()
        c.close()
        conn.close()