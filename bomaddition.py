

import sqlite3
import openpyxl
from openpyxl import load_workbook
import re

def slugify(text, lower=1):
    if lower == 1:
        text = text.strip().lower()
    #print(text)    
    text = re.sub(r'[^\w _-]+', '', text)
    
    text = re.sub(r'[- ]+', '_', text)
    #print(text)
    return text

# database name
conn = sqlite3.connect("bommaddition.db")
# excel workbook
wb = load_workbook(filename = filename2)#r'trial1.xlsx')

sheets = wb.get_sheet_names()

for sheet in sheets:
    ws = wb[sheet] 

    columns= []
    query = 'CREATE TABLE IF NOT EXISTS ' + 'bommaddition ' + '(id INTEGER PRIMARY KEY'
    for row in next(ws.rows):
        query += ', ' + slugify(row.value) + ' TEXT'
        columns.append(slugify(row.value))
    query += ');'
    ##print(query)

    conn.execute("CREATE TABLE  IF NOT EXISTS  bommaddition (id INTEGER PRIMARY KEY, project TEXT, customer TEXT, dut INTEGER,stackup INTEGER,totalio INTEGER, pcbcomp INTEGER, testerconfig TEXT, power INTEGER, shape INTEGER, dimension TEXT, electrical INTEGER, c_pwr INTEGER, sig INTEGER, ground INTEGER, dc INTEGER, tpower INTEGER, pipwr INTEGER, diffio INTEGER, lmg INTEGER, otherio INTEGER, totaprobes INTEGER, tst INTEGER, bga TEXT,dummy INTEGER, capacitor INTEGER , relays INTEGER,ic INTEGER )")

    tup = []
    for i, rows in enumerate(ws):
        tuprow = []
        if i == 0:
            continue
        for row in rows:
            tuprow.append(str(row.value).strip()) if str(row.value).strip() != 'None' else tuprow.append('')
            #print(tuprow)
        tup.append(tuple(tuprow))


    insQuery1 = 'INSERT INTO ' + 'bommaddition ' + '('
    insQuery2 = ''
    for col in columns:
        insQuery1 += col + ', '
        insQuery2 += '?, '
   
    insQuery1 = insQuery1[:-2] + ') VALUES('
    insQuery2 = insQuery2[:-2] + ')'
    insQuery = insQuery1 + insQuery2
    

    conn.executemany(insQuery, tup)
    conn.commit()
    
    
    
    
def view():
    conn = sqlite3.connect("bommaddition.db")
    cur = conn.cursor()    
    cur.execute("SELECT * FROM  bommaddition")
    rows  = cur.fetchall()
    conn.close()      
    return rows 


def removebrac(text):
    
    #print(text)    
    text = re.sub(r'[^\w _-]+', '', text)
    
    
    print(text)
    return text
#print(removebrac("{abhi}"))
conn.close()
#print(view())