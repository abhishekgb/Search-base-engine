#Program Writen by Abhishek Gubbi Basavaraj
import sqlite3
from tkinter import ttk
import csv
from xlsxwriter.workbook import Workbook

def connect():
    conn = sqlite3.connect('design1n3.db')
    cur = conn.cursor()
    conn.execute("CREATE TABLE  IF NOT EXISTS  design1n5 (id INTEGER PRIMARY KEY, project TEXT, customer TEXT, dut INTEGER,stackup INTEGER,totalio INTEGER, pcbcomp INTEGER, testerconfig TEXT, power INTEGER, shape INTEGER, dimension TEXT, electrical INTEGER, c_pwr INTEGER, sig INTEGER, ground INTEGER, dc INTEGER, tpower INTEGER, pipwr INTEGER, diffio INTEGER, lmg INTEGER, otherio INTEGER, totaprobes INTEGER, pcbtype INTEGER, bga TEXT,dummy INTEGER,capacitor INTEGER , relays INTEGER,ic INTEGER,bgapitch TEXT)")
    conn.commit()
    conn.close()
    
    
def insert(project , customer , dut ,stackup , totalio , pcbcomp , testerconfig , power , shape , dimension , electrical , pwr , sig , ground , dc , tpower , pipwr , diffio , lmg , otherio , totapr , pcbtype , bga,capacitor,relays,ic,bgapitch):
    conn = sqlite3.connect('design1n3.db')
    cur = conn.cursor()    
    cur.execute("INSERT INTO design1n5 VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,1)",(project , customer , dut ,stackup , totalio , pcbcomp , testerconfig , power , shape , dimension , electrical , pwr , sig , ground , dc , tpower , pipwr , diffio , lmg , otherio , totapr , pcbtype , bga,capacitor,relays,ic,bgapitch))
    conn.commit()
    conn.close()    
    


def view():
      
    conn = sqlite3.connect('design1n3.db')
    cur = conn.cursor()  
    cur.execute("SELECT id,project,customer FROM design1n5")
    rows  = cur.fetchall()         
    
    conn.close()        
    return rows





    
def view_e():
    workbook = Workbook('allveiw.xlsx')
    worksheet = workbook.add_worksheet()    
    conn = sqlite3.connect('design1n3.db')
    cur = conn.cursor()  
    cur.execute("SELECT id,project,customer FROM design1n5")
    rows  = cur.fetchall()         
    heading = ["id","project" , "customer" , "dut" ,"stackup" , "totalio" , "pcbcomp" , "testerconfig" , "power" , "shape" , "dimension" , "electrical" , "pwr" , "sig" , "ground" , "dc" , "tpower" , "pipwr" , "diffio" , "lmg" , "otherio ", "totapr" , "pcbtype" , "bga","dummy","capacitor","relays","ic","bgapitch"]  
    for j1, name in enumerate(heading):
        worksheet.write(0, j1, name) 
        
        
    
    #conn.row_factory=sqlite3.Row  
    mysel= cur.execute("SELECT * FROM design1n3")
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i+1, j, row[j])                
    workbook.close() 
    conn.close()        
    return rows

def search(project  = "", customer  = "", dut  = "",stackup = "", totalio  = "", pcbcomp  = "", testerconfig  = "", power  = "", shape  = "", dimension  = "", electrical  = "", pwr  = "", sig  = "", ground  = "", dc  = "", tpower  = "", pipwr  = "", diffio  = "", lmg  = "", otherio  = "", totapr  = "", pcbtype  = "", bga  = "",capacitor= "",relays= "",ic= ""):
    conn = sqlite3.connect('design1n3.db')
    cur = conn.cursor()    
    cha12 = "SELECT * FROM  design1n5 WHERE ( project  = ? OR customer  = ? AND dut  = ? OR  stackup  = ? OR totalio  > ? OR pcbcomp  = ? OR testerconfig  = ? OR power  = ? OR shape  = ? OR dimension  = ? OR electrical  = ? OR c_pwr  = ? OR sig  = ? OR ground  = ? OR dc  = ? OR tpower  = ? OR pipwr  = ? OR diffio  = ? OR lmg  = ? OR otherio  = ? OR totaprobes  = ? OR pcbtype  = ? OR bga = ? AND dummy = 1)"
    cur.execute(cha12,(project , customer , dut ,stackup ,totalio , pcbcomp , testerconfig , power , shape , dimension , electrical , pwr , sig , ground , dc , tpower , pipwr , diffio , lmg , otherio , totapr , pcbtype , bga))
    
    rows  = cur.fetchall()
    conn.close()  
    return rows



def searchdesign(project):
    conn = sqlite3.connect('design1n3.db')
    cur = conn.cursor()
    cur.execute("SELECT  * FROM  design1n5 WHERE project = ? "(project,))
    dlist = cur.fetchall()
    conn.close()  
    return dlist

def custsearch():
    conn = sqlite3.connect('design1n3.db')
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT customer FROM  design1n5")
    dlist = cur.fetchall()
    conn.close()  
    return dlist  

def projsearch():
    conn = sqlite3.connect('design1n3.db')
    conn.row_factory = lambda cursor, row: row[0]
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT project FROM  design1n5")
    dlist = cur.fetchall()
    conn.close()  
    return dlist 


 
     
def dutsearch():
    conn = sqlite3.connect('design1n3.db')
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT dut FROM  design1n5")
    dlist = cur.fetchall()
    conn.close()  
    return dlist 

def shapesearch():
    conn = sqlite3.connect('design1n3.db')
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT shape FROM  design1n5")
    dlist = cur.fetchall()
    conn.close()  
    return dlist 


def testerconfigsearch():
    conn = sqlite3.connect('design1n3.db')
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT testerconfig FROM  design1n5")
    dlist = cur.fetchall()
    conn.close()  
    return dlist 
     

       
 
def tempch():
    conn = sqlite3.connect('design1n3.db')
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT pcbtype FROM  design1n5")
    dlist = cur.fetchall()
    conn.close()  
    return dlist  

 
def stacksearch():
    conn = sqlite3.connect('design1n3.db')
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT stackup FROM  design1n5")
    dlist = cur.fetchall()
    conn.close()  
    return dlist                  

def delete(id):
    conn = sqlite3.connect('design1n3.db')
    cur = conn.cursor()    
    cur.execute("DELETE FROM  design1n5 WHERE id = ?",(id,))
    
    conn.commit()
    conn.close()
    
                

        
        


def searchdesign1(id):
    conn = sqlite3.connect('design1n3.db')
    cur = conn.cursor()    
    cur.execute("SELECT * FROM  design1n5 WHERE id = ?",(id,))
    dlist1 = cur.fetchall()
    conn.commit()
    conn.close()  
    #print(dlist1)
    return dlist1[0]    
    
def update(id,project , customer , dut  ,stackup , totalio , pcbcomp , testerconfig , power , shape , dimension , electrical , pwr , sig , ground , dc , tpower , pipwr , diffio , lmg , otherio , totapr , pcbtype , bga,capacitor,relays,ic,bgapitch):
    conn = sqlite3.connect('design1n3.db')
    cur = conn.cursor()    
    dummy = 1
    cur.execute("UPDATE  design1n5 SET project    = ? ,  customer    = ? ,  dut    = ? ,   stackup    = ? ,  totalio    = ? ,  pcbcomp    = ? ,  testerconfig    = ? ,  power    = ? ,  shape    = ? ,  dimension    = ? ,  electrical    = ? ,  c_pwr    = ? ,  sig    = ? ,  ground    = ? ,  dc    = ? ,  tpower    = ? ,  pipwr    = ? ,  diffio    = ? ,  lmg    = ? ,  otherio    = ? ,  totaprobes    = ? ,  pcbtype    = ? ,  bga  = ? ,dummy = ?,capacitor = ?,relays = ?,ic = ?,bgapitch = ? WHERE id = ?",(project , customer , dut  ,stackup , totalio , pcbcomp , testerconfig , power , shape , dimension , electrical , pwr , sig , ground , dc , tpower , pipwr , diffio , lmg , otherio , totapr , pcbtype , bga,dummy,capacitor,relays,ic,bgapitch,id))
    conn.commit()
    conn.close()    

#connect()
#insert("The python","superman",1918,1902)
#delete(1)
#update(1,"heman","abhishek",1990,98765,5,5,5,5,5,5)
#print(view())
#print(projsearch())
