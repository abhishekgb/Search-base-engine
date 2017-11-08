
#Program Writen by Abhishek Gubbi Basavaraj



#import pandas as pd
from tkinter import ttk
from tkinter import*
import  backend
import samplebomb
import webbrowser
from tkinter import messagebox
import  textgenerator
import os
import xlrd
import re
from tkinter import filedialog
from PIL import ImageTk, Image
import bombutton
class AutocompleteEntry(Entry):
    def __init__(self, lista, *args, **kwargs):
        # Listbox length
        if 'listboxLength' in kwargs:
            self.listboxLength = kwargs['listboxLength']
            
            del kwargs['listboxLength']
        else:
            self.listboxLength = 5
           
            
        # Custom matches function
        if 'matchesFunction' in kwargs:
            self.matchesFunction = kwargs['matchesFunction']
            del kwargs['matchesFunction']
        else:
            def matches(fieldValue, acListEntry):
                pattern = re.compile('.*' + re.escape(fieldValue) + '.*', re.IGNORECASE)
                return re.match(pattern, acListEntry)
                
            self.matchesFunction = matches            
            
        Entry.__init__(self, *args, **kwargs)
       
        self.lista = lista        
        AutocompleteEntry.var = self["textvariable"]
        self["width"] = 45
        self["font"] =("Helvetica", 12)
        if AutocompleteEntry.var == '':
            AutocompleteEntry.var = self["textvariable"] = StringVar()
        #print(AutocompleteEntry.var.get())
        AutocompleteEntry.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)
        
        self.lb_up = False

    def changed(self, name, index, mode):  

        if AutocompleteEntry.var.get() == '':
            if self.lb_up:
                self.lb.destroy()
                self.lb_up = False
        else:           
            words = self.comparison()
            if words:            
                if not self.lb_up:
                    self.lb = Listbox(width=self["width"], height=self.listboxLength)
                    #Double button is to select the line and make  it as selection 
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height())
                    self.lb_up = True
                
                self.lb.delete(0, END)
                for w in words:
                    self.lb.insert(END,w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False
        
    def selection(self, event):
        

        if self.lb_up:
            
            AutocompleteEntry.var.set(self.lb.get(ACTIVE))
            
           
            self.lb.destroy()
            self.lb_up = False
            self.icursor(END)
       
            
    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0': 
                
                self.lb.selection_clear(first=index)
                index = str(int(index)-1)                
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != END:                        
                self.lb.selection_clear(first=index)
                index = str(int(index)+1)        
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def comparison(self):
                
        pattern = re.compile('.*' + AutocompleteEntry.var.get() + '.*', re.IGNORECASE)
        return [w for w in self.lista if re.match(pattern, w)]


def treeview_list():
    
    global tree   
    tree = ttk.Treeview( window)
         
  
        
def get_selected_row(event):
        
        
    global selected_tuple
    selectline = 1
    #print(event)
    if (v41.get() == 1 ):#and (v50.get() !=1 or v49.get()!= 1)):
        
    #messagebox.showerror("Error", "Deselect Part search and Click Veiw all")
    #view_command()
        clear_command()
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        
        e1.delete(0,END)
        selted1 = "{" + selected_tuple[0] +"}"
        e1.insert(END,selted1)
        ##searchf_command()
        e41.delete(0,END)
        e41.insert(END,selected_tuple[1])
        print("prtokletssee")
        print(selected_tuple[1])
        trial12 = samplebomb.search_lv(selected_tuple[1])
        if (trial12 == []):
            print("empty detected")
            trial13 = samplebomb.search_lv_no(selected_tuple[1])
            e42.delete(0,END)
            e42.insert(END,trial13[0])
            #searchf_command()
            e43.delete(0,END)
            e43.insert(END,trial13[1])
            
            e81.delete(0,END)
            e81.insert(END,"not found")
            
            e91.delete(0,END)
            e91.insert(END,"not found")            
            
        else :
            print("ok no worry")
            print(trial12)
            e42.delete(0,END)
            e42.insert(END,trial12[0])
            #searchf_command()
            e43.delete(0,END)
            e43.insert(END,trial12[1])
            
            e81.delete(0,END)
            e81.insert(END,trial12[2])
            
            e91.delete(0,END)
            e91.insert(END,trial12[3])            
            
                 
#searchf_command()        
    elif(v50.get() !=1) :
        
        if (v49.get() !=1) :
                        
        
            if len(list1.curselection())>0:
                    index = list1.curselection()[0]
                    selected_tuple = list1.get(index)
                    selted = r"\\" 
                    selted2 =  "{"+ selected_tuple[1] +"}"
                    global project1_text 
                    project1_text = StringVar()
                    project1_text.get() 
                    e1.delete(0,END)
                    
                    e1.insert(END,selted2) 
                    trial2 = backend.searchdesign1(selected_tuple[0])
                    print(trial2[1])
                    trial1 = backend.searchdesign1(selected_tuple[0])
                    #print(trial1[1])
                    e2.delete(0,END)
                    e2.insert(END,trial1[2])                  
                                      
                            
                        
                       
                        #print(selted)
                        
                       
                        
                    e3.delete(0,END)
                    e3.insert(END,trial1[3])
                    
                    e4.delete(0,END)
                    e4.insert(END,trial1[4]) 
                    
                    e5.delete(0,END)
                    e5.insert(END,trial1[5]) 
                    
                    e6.delete(0,END)
                    e6.insert(END,trial1[6])
                    
                    e7.delete(0,END)
                    e7.insert(END,trial1[7])
                    
                    e8.delete(0,END)
                    e8.insert(END,trial1[8])
                    
                    e10.delete(0,END)
                    e10.insert(END,trial1[9])         
                
                    e11.delete(0,END)
                    e11.insert(END,trial1[10])
                    
                    e12.delete(0,END)
                    e12.insert(END,trial1[11])
                    
                    e13.delete(0,END)
                    e13.insert(END,trial1[12])
                    
                    e14.delete(0,END)
                    e14.insert(END,trial1[13]) 
                    
                    e15.delete(0,END)
                    e15.insert(END,trial1[14]) 
                    
                    e16.delete(0,END)
                    e16.insert(END,trial1[15])
                    
                    e17.delete(0,END)
                    e17.insert(END,trial1[16])
                    
                    e18.delete(0,END)
                    e18.insert(END,trial1[17])
                    
                    e19.delete(0,END)
                    e19.insert(END,trial1[18])        
                     
                    
                    e20.delete(0,END)
                    e20.insert(END,trial1[19])
                           
                
                    e21.delete(0,END)
                    e21.insert(END,trial1[20])
                    
                    e22.delete(0,END)
                    e22.insert(END,trial1[21])
                    
                    e23.delete(0,END)
                    e23.insert(END,trial1[22])
                    
                    e24.delete(0,END)
                    e24.insert(END,trial1[23])  
                    
                    e25.delete(0,END)
                    e25.insert(END,trial1[24]) 
                    
                    e51.delete(0,END)
                    e51.insert(END,trial1[25])
                    
                    e61.delete(0,END)
                    e61.insert(END,trial1[26])  
                    
                    e71.delete(0,END)
                    e71.insert(END,trial1[27]) 
                   
                    
                    e101.delete(0,END)
                    e101.insert(END,final)  
                    
                    e28.delete(0,END)
                    e28.insert(END,trial1[24])                
   

  

def view_command():
   
    if v17.get() == 1:
        
        view_command_e()
    else :
        view_command_ne()
 
def view_command_e():
    if  v41.get() == 1:
        list1.delete(0,END)
               
        
    else :
        
          
        list1.delete(0,END)
        for row in backend.view_e():
            list1.insert(END,row) 
        

def view_command_ne():
    if  v41.get() == 1:
        list1.delete(0,END)
               
        
    else :
        
          
        list1.delete(0,END)
        for row in backend.view():
            list1.insert(END,row)
        
#def searchf_command():
    #textgenerator.check_text(project_text.get(), customer_text.get(), dut_text.get(),stackup_text.get(), TotalIO_text.get(), PCBcomp_text.get(), Testerconfig_text.get(), power_text.get(), Shape_text.get(), dimension_text.get(), Electrical_text.get(), pwr_text.get(), sig_text.get(), ground_text.get(), DC_text.get(), Tpower_text.get(), Pipwr_text.get(), DiffIO_text.get(), LMG_text.get(), Otherio_text.get(), Totapr_text.get(), tst_text.get(), BGA_text.get())
    
def searchf_command():
    if  v41.get() == 1:
        searchpart_command()
        
    else :
        
        
        
           
        list1.delete(0,END)
        
        for row in textgenerator.check_text(project_text.get(),customer_text.get(), dut_text.get(),stackup_text.get(), TotalIO_text.get(), PCBcomp_text.get(), Testerconfig_text.get(), power_text.get(), Shape_text.get(), dimension_text.get(), Electrical_text.get(), pwr_text.get(), sig_text.get(), ground_text.get(), DC_text.get(), Tpower_text.get(), Pipwr_text.get(), DiffIO_text.get(), LMG_text.get(), Otherio_text.get(), Totapr_text.get(), tst_text.get(), BGA_text.get(),capacitor_text.get(),relay_text.get(),ic_text.get(),dut_select.get() , stackup_select.get() , ttio_select.get() , pcb_select.get() , powerlayer_select.get() , electricallayer_select.get() , criticallayer__select.get() , signallayer_select.get() , groundlayer_select.get() , DC_layer_select.get() , Ttlpowr_Nets_select.get() ,PIpwr_Nets_select.get() , diffio_Nets_select.get() , lmg_layer_select.get() , Otherio_Layer_select.get() , Totalprobes_select.get(),cap_select.get(),Relay_select.get(),IC_select.get(),v17.get(),pitch_text.get()):
            row1 = row
            #list1.insert(row[0])
            list1.insert(END,row)

        

def add_command():
    if  v16.get() == 1 or ( v1.get() and  v2.get() and  v3.get() and  v4.get() and  v5.get() and  v6.get() and  v7.get() and  v8.get() and  v9.get() and  v10.get() and  v11.get() and  v12.get() and  v13.get() and  v14.get() and  v15.get()):
        backend.insert(project_text.get(), customer_text.get(), dut_text.get(),stackup_text.get(), TotalIO_text.get(), PCBcomp_text.get(), Testerconfig_text.get(), power_text.get(), Shape_text.get(), dimension_text.get(), Electrical_text.get(), pwr_text.get(), sig_text.get(), ground_text.get(), DC_text.get(), Tpower_text.get(), Pipwr_text.get(), DiffIO_text.get(), LMG_text.get(), Otherio_text.get(), Totapr_text.get(), tst_text.get(), BGA_text.get(),capacitor_text.get(),relay_text.get(),ic_text.get(),pitch_text.get())
        result = messagebox.askquestion("addition", "Click yes to confirm addition", icon='warning')
        if result == 'yes':
            print ("Deleted")
            list1.delete(0,END)
            list1.insert(END,(0,project_text.get(), customer_text.get(), dut_text.get(),stackup_text.get(), TotalIO_text.get(), PCBcomp_text.get(), Testerconfig_text.get(), power_text.get(), Shape_text.get(), dimension_text.get(), Electrical_text.get(), pwr_text.get(), sig_text.get(), ground_text.get(), DC_text.get(), Tpower_text.get(), Pipwr_text.get(), DiffIO_text.get(), LMG_text.get(), Otherio_text.get(), Totapr_text.get(), tst_text.get(), BGA_text.get(),capacitor_text.get(),relay_text.get(),ic_text.get(),pitch_text.get()))

        else:
            print ("I'm Not Deleted Yet")
       
    else :
        # message box display  
        messagebox.showerror("Error", "Select all Fields and Select the row to update")  
        
def delete_command():
    result = messagebox.askquestion("Delete", "Click yes to confirm delete", icon='warning')
    if result == 'yes':
        print ("Deleted")
        backend.delete(selected_tuple[0])
    else:
        print ("I'm Not Deleted Yet")
    
    
def update_command():
    
    project_text1 =  re.sub('[{}]', '', project_text.get())
    if  v16.get() == 1 or ( v1.get() and  v2.get() and  v3.get() and  v4.get() and  v5.get() and  v6.get() and  v7.get() and  v8.get() and  v9.get() and  v10.get() and  v11.get() and  v12.get() and  v13.get() and  v14.get() and  v12.get()):
      
        backend.update(selected_tuple[0],project_text1, customer_text.get(), dut_text.get(),stackup_text.get(), TotalIO_text.get(), PCBcomp_text.get(), Testerconfig_text.get(), power_text.get(), Shape_text.get(), dimension_text.get(), Electrical_text.get(), pwr_text.get(), sig_text.get(), ground_text.get(), DC_text.get(), Tpower_text.get(), Pipwr_text.get(), DiffIO_text.get(), LMG_text.get(), Otherio_text.get(), Totapr_text.get(), tst_text.get(), BGA_text.get(),capacitor_text.get(),relay_text.get(),ic_text.get(),pitch_text.get())
   # print(selected_tuple[0],project_text.get(), customer_text.get(), dut_text.get(),stackup_text.get(), TotalIO_text.get(), PCBcomp_text.get(), Testerconfig_text.get(), power_text.get(), Shape_text.get(), dimension_text.get(), Electrical_text.get(), pwr_text.get(), sig_text.get(), ground_text.get(), DC_text.get(), Tpower_text.get(), Pipwr_text.get(), DiffIO_text.get(), LMG_text.get(), Otherio_text.get(), Totapr_text.get(), tst_text.get(), BGA_text.get())
    else :
        # message box display
        messagebox.showerror("Error", "Select all Fields and Select the row to update")         
    
# additional entries--------------------------------------------------------------------

def shape_command():
    global l12
    global e10
    
    global Shape_text
    Shape_text = StringVar()
    e10 = ttk.Combobox(window)
    if (v1.get() == 1 or v16.get() == 1):
        
        
        
        l12 = Label(window,text ="PCB Shape")
        l12.grid(row = 4+x,column =0)         
        
    
        e10 = ttk.Combobox(window,textvariable = Shape_text,width = 12)
        e10.grid(row =4+x ,column = 1) 
        mylistdsh = backend.shapesearch()
        e10['values'] =['Rectangular','Circular']# tuple(mylistdsh)        
            
         #get_selected_row(event)#e10.insert(END,selected_tuple[9])
   
    
def dimension_command():
    global l13
    global e11
    global dimension_text
    dimension_text = StringVar()
    e11 = ttk.Combobox(window)
    if v2.get() == 1 or v16.get() == 1:
        l13 = Label(window,text ="Dimension of PCB")
        l13.grid(row = 4 + x,column =2) 
        dimension_text = StringVar()
    
        e11 = ttk.Combobox(window,textvariable = dimension_text,width = 12)
        e11.grid(row =4+ x ,column = 3) 
        #mylistdsh = backend.Shapesearch()
        e11['values'] =['22900x16900','1100']        
        #get_selected_row(event)#e11.insert(END,selected_tuple[10])
    
    
def Electrical_Layer():
    global l14
    global e12
    global Electrical_text
    e12 = ttk.Combobox(window)
    Electrical_text = StringVar()
    global electricallayer_select
    electricallayer_select = StringVar(window)
    if v3.get() == 1 or v16.get() == 1:
        
        
        
        electricallayer_select.set("ElectricalLay_=") # default value
        
        
      
        
        l14 =OptionMenu(window, electricallayer_select, "ElectricalLay_>", "ElectricalLay_<", "ElectricalLay_=")
        l14.grid(row = 5+ x,column =0) 
        
        
        e12 = ttk.Combobox(window,textvariable = Electrical_text,width = 12)
        e12.grid(row =5+ x ,column = 1) 
        e12['values'] =['36','56','37']
        # get_selected_row(1)#e12.insert(END,selected_tuple[11])
   
    
def cPower_Layer():
    global l15
    global e13
    global pwr_text
    pwr_text = StringVar()
    global criticallayer__select
    criticallayer__select = StringVar(window)
    e13 = ttk.Combobox(window)
    if v4.get() == 1 or v16.get() == 1:
        
        
        
        criticallayer__select.set("criticallayer_=") # default value
        
        
      
        
              
        l15 = OptionMenu(window, criticallayer__select, "criticallayer_>", "criticallayer_<", "criticallayer_=") 
        l15.grid(row = 5+ x,column =2) 
        pwr_text = StringVar()
        
        e13 = ttk.Combobox(window,textvariable = pwr_text,width = 12)
        e13.grid(row =5+ x ,column = 3) 
        e13['values'] =['20','17','18']
        # get_selected_row(1)#e13.insert(END,selected_tuple[12])


def Signal_Layer():
    global l16
    global e14
    global sig_text
    global signallayer_select
    signallayer_select = StringVar(window)
    sig_text = StringVar()
    e14 = ttk.Combobox(window)
    if v5.get() == 1 or v16.get() == 1:
        
        
        signallayer_select.set("signallayer_=") # default value
        
        l16 = OptionMenu(window, signallayer_select, "signallayer_>", "signallayer_<", "signallayer_=") 
        
        
        l16.grid(row = 6+ x,column =0) 
        sig_text = StringVar()
        
        e14 = ttk.Combobox(window,textvariable = sig_text,width = 12)
        e14.grid(row =6+ x ,column = 1) 
       
        e14['values'] =['12','13','14']        
        # get_selected_row(1)#e14.insert(END,selected_tuple[13])
    
def ground_command():
    global l17
    global e15
    global ground_text
    global groundlayer_select
    groundlayer_select = StringVar(window)
    ground_text = StringVar()
    e15 = ttk.Combobox(window)
    if v6.get() == 1 or v16.get() == 1:
        
        
        
       
        groundlayer_select.set("groundlayer_=") # default value
        

        l17 = OptionMenu(window, groundlayer_select, "groundlayer_>", "groundlayer_<", "groundlayer_=")
        l17.grid(row = 6+ x,column =2) 
        
        
        e15 = ttk.Combobox(window,textvariable = ground_text,width = 12)
        e15.grid(row =6+ x ,column = 3) 
       #  get_selected_row(1)#e15.insert(END,selected_tuple[14])
   
    
def DC_Layer():
    global l18
    global e16
    global DC_text
    global DC_layer_select
    global DC_layer_select
    DC_layer_select = StringVar(window)
    DC_text = StringVar()
    e16 = ttk.Combobox(window)
    if v7.get() == 1 or v16.get() == 1:
        
        
       
        DC_layer_select.set("DC_layer_=") # default value
        
       
        
        
        l18 = OptionMenu(window, DC_layer_select, "DC_layer_>", "DC_layer_<", "DC_layer_=") 
        l18.grid(row = 7+ x,column =0) 
        
        
        e16 = ttk.Combobox(window,textvariable = DC_text,width = 12)
        e16.grid(row =7+ x ,column = 1) 
       #  get_selected_row(1)#e16.insert(END,selected_tuple[15])
    
    
def totPower_Layer():
    global l19
    global e17
    global Tpower_text
    global Ttlpowr_Nets_select
    Ttlpowr_Nets_select = StringVar(window)
    Tpower_text = StringVar()
    e17 = ttk.Combobox(window)
    if v8.get() == 1 or v16.get() == 1:
        
        
       
        Ttlpowr_Nets_select.set("Ttlpowr_Nets_=") # default value
        
       
       
        l19 = OptionMenu(window, Ttlpowr_Nets_select, "Ttlpowr_Nets_>", "Ttlpowr_Nets_<", "Ttlpowr_Nets_=")
        l19.grid(row = 7+ x,column =2) 
        
        
        e17 = ttk.Combobox(window,textvariable = Tpower_text,width = 12)
        e17.grid(row =7+ x ,column = 3) 
       #  get_selected_row(1)#e17.insert(END,selected_tuple[16])
   
    
def PIpo_Layer():
    global l20
    global e18
    global Pipwr_text
    Pipwr_text = StringVar()
    e18 = ttk.Combobox(window)
    global  PIpwr_Nets_select
    PIpwr_Nets_select = StringVar(window)
    if v9.get() == 1 or v16.get() == 1:
        
        
       
        PIpwr_Nets_select.set("PIpwr_Nets_=") # default value
        
       
       
       
        
        
        l20  = OptionMenu(window, PIpwr_Nets_select, "PIpwr_Nets_>", "PIpwr_Nets_<", "PIpwr_Nets_=") 
        l20.grid(row = 8+ x,column =0) 
        Pipwr_text = StringVar()
        
        e18 = ttk.Combobox(window,textvariable = Pipwr_text,width = 12)
        e18.grid(row =8+ x ,column = 1) 
       #  get_selected_row(1)#e18.insert(END,selected_tuple[17])
    
def DiffIO_command():
    global l21
    global e19
    global DiffIO_text
    DiffIO_text = StringVar()
    e19 = ttk.Combobox(window)
    global diffio_Nets_select
    diffio_Nets_select = StringVar(window)  
    if v10.get() == 1 or v16.get() == 1:
        
       
        diffio_Nets_select.set("diffio_Nets_=") # default value
        
           
        
        l21 = OptionMenu(window, diffio_Nets_select, "diffio_Nets_>", "diffio_Nets_<", "diffio_Nets_=")  
        l21.grid(row = 8+ x,column =2) 
        
        
        e19 = ttk.Combobox(window,textvariable = DiffIO_text,width = 12)
        e19.grid(row =8+ x,column =3) 
        # get_selected_row(1)#e19.insert(END,selected_tuple[18])
   
    
def LMG_Layer():
    global l22
    global e20
    global LMG_text
    LMG_text = StringVar()
    e20 = ttk.Combobox(window)
    global lmg_layer_select
    lmg_layer_select = StringVar(window)
    if v11.get() == 1 or v16.get() == 1:
        
        lmg_layer_select = StringVar(window)
        lmg_layer_select.set("lmg_nets_=") # default value
        
           
        
     
        
        
        l22 = OptionMenu(window, lmg_layer_select, "lmg_nets_>", "lmg_nets_<", "lmg_nets_=")  
        l22.grid(row = 9+ x,column =0 )
        LMG_text = StringVar()
        
        e20 = ttk.Combobox(window,textvariable = LMG_text,width = 12)
        e20.grid(row =9+ x,column = 1) 
        # get_selected_row(1)#e20.insert(END,selected_tuple[19])
    
    
def Otherio_Layer():
    global l23
    global e21
    global Otherio_text
    Otherio_text = StringVar()
    e21 = ttk.Combobox(window)
    
    global Otherio_Layer_select
    Otherio_Layer_select = StringVar(window)
    if v12.get() == 1 or v16.get() == 1:
        
        Otherio_Layer_select = StringVar(window)
        Otherio_Layer_select.set("Otherio_nets_=") # default value
        
           
        
     
        
              
        l23 = OptionMenu(window, Otherio_Layer_select, "Otherio_nets_>", "Otherio_nets_<", "Otherio_nets_=")   
        l23.grid(row = 9+ x,column =2) 
        Otherio_text = StringVar()
        
        e21 = ttk.Combobox(window,textvariable = Otherio_text,width = 12)
        e21.grid(row =9+ x ,column = 3) 
       #  get_selected_row(1)# e21.insert(END,selected_tuple[20])
   
    
def Totapr_cmd():
    global l24
    global e22
    global Totapr_text
    Totapr_text = StringVar()
    e22 = ttk.Combobox(window)
    global Totalprobes_select
    Totalprobes_select = StringVar()    
    
    if v13.get() == 1 or v16.get() == 1:
        
        
        
       
        Totalprobes_select.set("Totalprobes_=") # default value
        
           
        
     
        
    
        l24 = OptionMenu(window, Totalprobes_select, "Totalprobes_>", "Totalprobes_<", "Totalprobes_=")
        l24.grid(row = 10+ x,column =0) 
        
        
        e22 = ttk.Combobox(window,textvariable = Totapr_text,width = 12)
        e22.grid(row =10+ x,column = 1)
        # get_selected_row(1)#e22.insert(END,selected_tuple[21])
  
def tst_temp():
    global l25
    global e23
    global tst_text
    tst_text = StringVar()
    e23 = ttk.Combobox(window)
    
    
    #global l31
    global e25
    global Dummy_text
    Dummy_text = StringVar()
    
       
    e25 = ttk.Combobox(window)    
    if v14.get() == 1 or v16.get() == 1:
        print("v14 =",v14.get(),"v16 =",v16.get())
        l25 = Label(window,text ="PCB Type")
        l25.grid(row =10+ x,column =2) 
       
        
        e23 = ttk.Combobox(window,textvariable = tst_text,width = 12)
        e23.grid(row =10+ x ,column = 3) 
        mylisttesttem =tuple(backend.tempch())
        e23['values']=mylisttesttem  #"-20C to 90","-20C to 90C",'20C']
        #get_selected_row()
       #  get_selected_row(1)#e23.insert(END,selected_tuple[24])
        
        #Dummy_text = StringVar()
        
        #l31 = Label(window,text ="Dummy")
        #l31.grid(row = 11+ x,column =2)  
        #e25 = Entry(window,textvariable = Dummy_text,width = 23)
        #e25.grid(row =11+ x ,column = 3)        
      #   get_selected_row(1)# e25.insert(END,selected_tuple[22])
        
        
   
    
def BGA_Dimen():
    global l26
    global e24
    global BGA_text
    global l28
    global e28
    global pitch_text    
    
    BGA_text = StringVar()
    e24 = ttk.Combobox(window)
    e28 = ttk.Combobox(window)
    BGA_selct =StringVar()
    pitch_text = StringVar()
    if v15.get() == 1 or v16.get() == 1:
        BGA_selct.set("BGA Dimen")
        l26 = OptionMenu(window,BGA_selct,"BGA Dimen")
        l26.grid(row = 11+ x,column =0) 
        
        
        BGA_text = StringVar()
        
        e24 = ttk.Combobox(window,textvariable = BGA_text,width = 12)
        e24.grid(row =11+ x ,column = 1)   
        
        l28 = Label(window,text ="BGA Pitch")
        l28.grid(row = 12+ x,column =0) 
        
        
       
        
        e28 = ttk.Combobox(window,textvariable = pitch_text,width = 12)
        e28.grid(row =12+ x ,column = 1)           
        
        e24['values'] =['60x60','74x74','64x64','88x88','80x80','32x32','72x72','66x66','94x94','42x42','56x56','20x20','20x20','48x48','44x44']
       # get_selected_row(1)#e24.insert(END,selected_tuple[23])
        #l27 = Label(window,text ="BGA Dimen")
        #l27.grid(row = 12,column =0)         
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# -----------------------------------------------------------------------------------------------------------   
def check():
    print(v1.get()) 
    if (v1.get() == 1 or v16.get() == 1):
        shape_command()
    else:
        e10.destroy()
        l12.destroy() 
        
        
def check1():        
    if v2.get() == 1 or v16.get() == 1:
        dimension_command()
    else:
        e11.destroy()
        l13.destroy() 
def check2():        
        
    if v3.get() == 1 or v16.get() == 1:
        Electrical_Layer()
    else:
        e12.destroy()
        l14.destroy()    
def check3():        
        
    if v4.get() == 1 or v16.get() == 1:
        cPower_Layer()
    else:
        e13.destroy()
        l15.destroy() 
        
def check4():        
    if v5.get() == 1 or v16.get() == 1:
        Signal_Layer()
    else:
        e14.destroy()
        l16.destroy()         
        
def check5():        
    if v6.get() == 1 or v16.get() == 1:
        ground_command()
    else:
        e15.destroy()
        l17.destroy() 
        
        
def check6():        
        
    if v7.get() == 1 or v16.get() == 1:
        DC_Layer()
    else:
        e16.destroy()
        l18.destroy()    
def check7():        
        
    if v8.get() == 1 or v16.get() == 1:
        totPower_Layer()
    else:
        e17.destroy()
        l19.destroy() 
        
def check8():        
    if v9.get() == 1 or v16.get() == 1:
        PIpo_Layer()
    else:
        e18.destroy()
        l20.destroy()         
        
               
def check9():        
    if v10.get() == 1 or v16.get() == 1:
        DiffIO_command()
    else:
        e19.destroy()
        l21.destroy() 
def check10():        
        
    if v11.get() == 1 or v16.get() == 1:
        LMG_Layer()
    else:
        e20.destroy()
        l22.destroy()    
def check11():        
        
    if v12.get() == 1 or v16.get() == 1:
        Otherio_Layer()
    else:
        e21.destroy()
        l23.destroy() 
        
def check12():        
    if v13.get() == 1 or v16.get() == 1:
        Totapr_cmd()
    else:
        e22.destroy()
        l24.destroy()         
        
def check13():        
        
    if v14.get() == 1 or v16.get() == 1:
        tst_temp()
    else:
        e23.destroy()
        l25.destroy() 
        e25.destroy()
        #l31.destroy()        
        
        
def check14():        
        
    if v15.get() == 1 or v16.get() == 1:
        BGA_Dimen()
    else:
        e24.destroy()
        l26.destroy() 
        e28.destroy()
        l28.destroy()        
        
        

def signin():
    
    def login_btn_clickked():
        #print("Clicked")
        username =entry_1.get()
        password =entry_2.get()
    
        #print(username, password)
    
        if username == "Admin" and password == "password":
            messagebox.showinfo("Login info", "Welcome Admin")
            window.wm_title("Logged INN")
            
        else:
            messagebox.showerror("Login error", "Incorrect username")   
            
            
    root1 = Toplevel(window)
    root1.title('Sign in ')
    root1.geometry("598x120+250+100")
    
    label_1 = Label(root1, text="Username")
    label_2 = Label(root1, text="Password")

    entry_1 = Entry(root1)
    entry_2 = Entry(root1, show="*")
 
    label_1.grid(row=0, sticky=E)
    label_2.grid(row=1, sticky=E)
    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)
    
    checkbox = Checkbutton(root1, text="Keep me logged in")
    checkbox.grid(columnspan=2)

    logbtn = Button(root1, text="Login", command =login_btn_clickked)
    logbtn.grid(columnspan=2)

    

    
    


def addwindwow():
    
    if project_text.get()  !="":
        #projectname =project_text.get()
        projectname=re.sub('[{}]', '', project_text.get())
        bombutton.callback(projectname,customer_text.get())
        #samplebomb.search_projectbased(project_text.get())
        messagebox.showerror("BOM addition done for ", projectname)
    else :
        messagebox.showerror("Error", "enter the project name ") 
        
def Partextraction():
    if (project_text.get()) !="":
        projectname =project_text.get()
        #bombutton.callback(projectname,customer_text.get())
        list1.delete(0,END)
        
        if (v50.get() == 1):
            if (v17.get() == 1):
                #samplebomb.search_projectexcel(re.sub('[{}]', '',project_text.get()))
                
            #samplebomb.search_projectbaseddiste(re.sub('[{}]', '',project_text.get()))
                
                for row in samplebomb.search_projectexcel(re.sub('[{}]', '',project_text.get())):
                    
                    rw12 = samplebomb.search_type(row[0])
                    #print(rw12)
                    rw13 = re.sub(r'[^\w _-]+', '', str(rw12))                
                    rownew = row[0]+'         ' +row[1]+'  '+rw13
                    list1.insert(END,rownew)                
            else :
                for row in samplebomb.search_projectbased(re.sub('[{}]', '',project_text.get())):
                    
                    rw12 = samplebomb.search_type(row[0])
                   # print(rw12)
                    rw13 = re.sub(r'[^\w _-]+', '', str(rw12))                
                    rownew = row[0]+'         ' +row[1]+'  '+rw13
                    list1.insert(END,rownew)                
                 
                                  
                 
            
            
        if (v49.get() == 1):
            
            
            if (v17.get() == 1):
                #samplebomb.search_projectbaseddiste(re.sub('[{}]', '',project_text.get()))
                for row in samplebomb.search_projectbaseddiste(re.sub('[{}]', '',project_text.get())):
                    
                    rw12 = samplebomb.search_type(row[0])
                   # print(rw12)
                    rw13 = re.sub(r'[^\w _-]+', '', str(rw12))
                    rownew = str(row[0])+'  ' +'   '+str(rw13)+'   '+ str(row[2])+'       '+str(row[1])
                    #print("debugging")
                    #print(row[1])
                    list1.insert(END,rownew)  
            else :
                for row in samplebomb.search_projectbaseddist(re.sub('[{}]', '',project_text.get())):
                    
                    rw12 = samplebomb.search_type(row[0])
                   # print(rw12)
                    rw13 = re.sub(r'[^\w _-]+', '', str(rw12))
                    rownew = str(row[0])+'  ' +'   '+str(rw13)+'   '+ str(row[2])+'       '+str(row[1])
                   # print("debugging")
                   # print(row[1])
                    list1.insert(END,rownew)                      
                 
               
                        
               
            
            
        
    else :
        messagebox.showerror("Error", "enter the project name ")    
    
    
def DeleteBOM():
    if (project_text.get()) !="":
        result = messagebox.askquestion("Delete", "Click yes to confirm delete", icon='warning')
        if result == 'yes':
            print ("Deleted")
            samplebomb.deletebom(project_text.get())
        else:
            print ("I'm Not Deleted Yet")
        
        
        
        
    else :
        messagebox.showerror("Error", "enter the project name ")     
    
     
    
    #def open_file():
        #global content
        #global file_path
        #global filename

        #filename = filedialog.askopenfilename()
        ##infile = open(filename, 'r')
        ##content = infile.read()
        #file_path = os.path.dirname(filename)
        
        #entry.delete(0, END)
        #entry.insert(0, file_path)    
        #return filename 
    
    #def process_file():
        #print ("hai")  
        #print(filename)
        #filename2 = " C:\Users\abasavaraj\Documents\python codes\database for testing\Better GUI\with multilist\BOM1.xlsx"
              
        #wb = file_path
        
        #sheets = wb.get_sheet_names()        
       
    #root = Toplevel(window)
    #root.title('BOM adder')
    #root.geometry("598x120+250+100")
    
    #mf = Frame(root)
    #mf.pack()
    
    
    #f1 = Frame(mf, width=600, height=250)
    #f1.pack(fill=X)
    #f2 = Frame(mf, width=600, height=250)
    #f2.pack()
    
    #file_path = StringVar
    
    
    #Label(f1,text="Select Bom File (Only excel files)").grid(row=0, column=0, sticky='e')
    #entry = Entry(f1, width=50, textvariable=file_path)
    #entry.grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=25)
    #Button(f1, text="Browse", command=open_file).grid(row=0, column=27, sticky='ew', padx=8, pady=4)
    #Button(f2, text="ADD to DataBase", width=32, command= process_file).grid(sticky='ew', padx=10, pady=10)    
    


def p1_command():
    window1 = Toplevel(window)
    window1.geometry("200x400")
    window1.wm_title("More") 
    #----label in page
    #l11 = Label(window1,text ="Select")
    #l11.grid(row = 0,column =0)
    
    #-----check buttons
   # global v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15
       
    
    
    
    
    

    c1 = Checkbutton(window1, text ="Shape",variable = v1,command = check,wraplength = 60)
    c1.grid(row = 0,column = 0)      
    
    c2 = Checkbutton(window1, text ="Dimensions",variable = v2,command = check1,wraplength = 60)
    c2.grid(row = 1,column = 0)
    
    c3 = Checkbutton(window1, text ="# of Electrical Layer",variable = v3,command = check2,wraplength = 60)
    c3.grid(row = 2,column = 0)
    
    c4 = Checkbutton(window1, text ="# cr Power Layers",variable = v4,command = check3,wraplength = 60,)
    c4.grid(row = 3,column = 0)    
    
    c5 = Checkbutton(window1,text = "# Signal Layer",variable = v5,command = check4,wraplength = 60)
    c5.grid(row = 4,column = 0) 
    
    c14 = Checkbutton(window1, text ="# Ground Layers",variable = v6,command = check5,wraplength = 60)
    c14.grid(row = 5,column =0)    
    
    c15 = Checkbutton(window1,text = "# Dc layer Layer",variable = v7,command = check6,wraplength = 60)
    c15.grid(row = 6,column = 0) 
    
    c6 = Checkbutton(window1, text ="Total power nets",variable = v8,command = check7,wraplength = 60)
    c6.grid(row = 7,column =0)  
    
    c13 = Checkbutton(window1,text = "# PI power nets",variable = v9,command = check8,wraplength = 60)
    c13.grid(row = 0,column = 6)      
    
    c7 = Checkbutton(window1, text ="Diff IO's",variable = v10,command = check9,wraplength = 60)
    c7.grid(row = 1,column = 6)
    
    c8 = Checkbutton(window1, text ="Lenght Matching IO's",variable = v11,command = check10,wraplength = 60)
    c8.grid(row = 2,column = 6)
    
    c9 = Checkbutton(window1, text ="Other IO's",variable = v12,command = check11,wraplength = 60)
    c9.grid(row = 3,column = 6)    
    
    c10 = Checkbutton(window1,text = "Total Probes",variable = v13,command = check12,wraplength = 60)
    c10.grid(row = 4,column = 6) 
    
    c11 = Checkbutton(window1, text ="Type of PCB",variable = v14,command = check13,wraplength = 60)
    c11.grid(row = 5,column = 6)    
    
    c12 = Checkbutton(window1,text = "# BGA Dimensions",variable = v15,command = check14,wraplength = 60)
    c12.grid(row =6,column = 6)  
    
    #b8 = Button(window1,text = "Select all ",width = 12,command = selectall_command)
    #b8.grid(row = 0,column = 8) 
    
    c13 = Checkbutton(window1,text = "Select all",variable = v16,command = selectall_command,wraplength = 60)
    c13.grid(row =7,column = 6)      
    
    
    
    # button lists
    #b8 = Button(window1,text = "check ",width = 10,command = check)
    #b8.grid(row = 2,column = 1) 
    
def selectall_command():
    
    
    check()
    check1()
    check2()
    check3()
    check4()
    check5()
    check6()
    check7()
    check8()
    check9()
    check10()
    check11()
    check12()
    check13()
    check14()

    
    
    
    
    
    
   
def clear_command():
    
    e1.delete(0,END)
   
    e2.delete(0,END)
    
    
    e3.delete(0,END)
  
    e4.delete(0,END)
   
    e5.delete(0,END)
   
    e6.delete(0,END)
    
    e7.delete(0,END)
  
    e8.delete(0,END)
    
    e11.delete(0,END)
    
    
    e10.delete(0,END)
    
    
    e12.delete(0,END)
    
    
    e13.delete(0,END)
  
    e14.delete(0,END)
   
    e15.delete(0,END)
   
    e16.delete(0,END)
    
    e17.delete(0,END)
  
    e18.delete(0,END)
    e19.delete(0,END)
    e21.delete(0,END)
    
    
    e20.delete(0,END) 
    e22.delete(0,END)
    
    
    e23.delete(0,END)
  
    e24.delete(0,END)  
    e25.delete(0,END)
    e28.delete(0,END)
    e51.delete(0,END)
  
    e61.delete(0,END)  
    e71.delete(0,END)    
      
    e41.delete(0,END)
   
    e42.delete(0,END)
    
    #searchf_command()
    e43.delete(0,END)
   
    
    e81.delete(0,END)
   
    
    e91.delete(0,END)
  
    e101.delete(0,END)  
      
      
      
def e2_onEnter(event):  
    
    mylist = backend.custsearch()
    print(mylist)
    
    # changes characters to upper case  
    customer_text.set(customer_text.get())  
    # gets the value of the text in the combobox. cbSymbol  
    mytext = customer_text.get() 
    # gets list of values from dropdwn list of  
    # cbSymbol combobox  
    vals = e2.cget('values')  
    # selects all in the combobox. cbSymbol  
    e2.select_range(0, END)  
    print(mytext)  
    # checks if symbol exists in the combobox if not it adds it  
    # to the dropdown list  
    if not vals:  
        
        
        e2.configure(values = (mytext, ))  
    elif mytext not in vals:   
        e2.configure(values = vals + (mytext, ))  
    return 'break'

#def pcb_command():
    #window2 = Toplevel(window)
    #window2.geometry("500x500")
    #window2.wm_title("PCB components")     
    
    ##label lists
    #lp1 = Label(window2,text ="Part Number")
    #lp1.grid(row = 0,column =60)
   
    #lp2 = Label(window2,text ="Project File")
    #lp2.grid(row = 3,column =60)
   
   
   
    ##entry  lists
   
    #part_text = StringVar()
    #ep1 = Entry(window2,textvariable = part_text)
    #ep1.grid(row =1 ,column = 60)
   
    #project_text = StringVar()
   
    #ep2 = Entry(window2,textvariable = project_text)
    #ep2.grid(row =4 ,column = 60)
    
def searchpart_command():
    global search_part
    search_part = 1
    list1.delete(0,END)
    #print(part_text.get())
    #tree.delete(*tree.get_children())
   
    global partdesign
    partdesign = tuple(samplebomb.search(part_text.get()))

    if part_text.get()== "":
         #messagebox.showerror("got it", "now add lv")
         if lv_text.get()== "":
             result2 = samplebomb.searchmpart(manupn_text.get())
             for row in samplebomb.searchmpart(manupn_text.get()):
                          
               
                 list1.insert(END,row)
             
                        
             
             
         else :
             
             
             result = samplebomb.search_lvsearch(lv_text.get())
             result1 = re.sub(r'[^\w _-]+', '', str(result))
             print("printing")
             print(result1)
             for row in samplebomb.search(result1):
                          
               
                 list1.insert(END,row)
    else: 
        if v17.get() == 1:
           
            for row in samplebomb.search_e(part_text.get()):
               
               
                list1.insert(END,row)   
        else:
            for row in samplebomb.search(part_text.get()):
                
                list1.insert(END,row)
               

               
        
         
           
         
    
        
        
  


def callback(event):
    webbrowser.open_new(hyper_text.get())


def login_click(*args):
    username = entry_1.get()
    password = entry_2.get()    
    print(username,password)
    
    if username == "admin" and password == "password":
        panel1.destroy()
        #messagebox.showinfo("Login info", "Welcome Admin")
        window.wm_title("PCB Database-V-12.0--admin")
        global path
        path = "logo.png"
        
        #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(window, image = img1)
        
        #The Pack geometry manager packs widgets in rows or columns.
        #panel.pack(side = "bottom", fill = "both", expand = "yes")
        panel.grid(row =13,column =0,rowspan = 14,columnspan = 3)        
        
        label_1.destroy()
        label_2.destroy()
        entry_1.destroy()
        entry_2.destroy()
        checkbox.destroy()
        logbtn.destroy()        
        
        global l1
        l1 = Label(window,text ="Project Name",fg="blue", cursor="hand2",font=("Helvetica", 12))
        l1.grid(row = 0,column =0,sticky = N)
        l1.bind("<Button-1>", callback)
        global l2
        l2 = Label(window,text ="Customer")
        l2.grid(row = 1,column =0,sticky = N)
        
        global dut_select
        dut_select = StringVar(window)
        dut_select.set("#_of_DUT_=") # default value
        
        global stackup_select
        stackup_select = StringVar(window)
        stackup_select.set("Stackup_Lay_=") # default value
        
        
        
        global l3
        l3 = OptionMenu(window, dut_select, "#_of_DUT_>", "#_of_DUT_<", "#_of_DUT_=")
        l3.grid(row = 2+x,column =0,sticky = N)
        global l4
        l4 = OptionMenu(window, stackup_select, "Stackup_Lay_>", "Stackup_Lay_<", "Stackup_Lay_=")
        l4.grid(row = 3+x,column =0,sticky = N)
        
        
        global ttio_select
        ttio_select = StringVar(window)
        ttio_select.set("Total_IO_=") # default value
        global l5
        l5 = OptionMenu(window, ttio_select, "Total_IO_<", "Total_IO_>", "Total_IO_=")
        l5.grid(row = 1,column =2,sticky = N)
        
        
        
        global pcb_select
        pcb_select = StringVar(window)
        pcb_select.set("pcb_comp_=") # default value
        
        global l6
        l6 = OptionMenu(window, pcb_select, "pcb_comp_>", "pcb_comp_<", "pcb_comp_=")
        l6.grid(row = 12,column =9,sticky = N)
        global l7
        l7 = Label(window,text ="Tester Configuration")
        l7.grid(row = 2+x,column =2,sticky = N)
        
        
        global powerlayer_select 
        powerlayer_select = StringVar(window)
        powerlayer_select.set("powerlayer_=") # default value
        
        global l8 
        l8 =  OptionMenu(window, powerlayer_select, "powerlayer_>", "powerlayer_<", "powerlayer_=")
        l8.grid(row = 3+x,column =2,sticky = N)
        
        
        #l9 = Label(window,text ="#signal_layer")
        #l9.grid(row = 3,column =2)
        
        #l10 = Label(window,text ="#ground_layer")
        #l10.grid(row = 4,column =2)
        

        
        #Customers =['QUALCOMM','SAMSUNG']
        
        #entry  lists
        global project_text 
        project_text = StringVar()
        #project_text.set(project_text.get().upper())
        global e1 
        global lista
        lista =backend.projsearch()
        
        print(lista)
        #e1["values"] = tuple(mylistp)        
        e1 = AutocompleteEntry(lista, window,width = 20)
        project_text = AutocompleteEntry.var 
        #print(e1("textvariable"))
        #e1 = ttk.Combobox(window,textvariable = project_text,width = 20)
        e1.grid(row =0,column = 1,columnspan = 3)
        global customer_text 
        customer_text = StringVar()        
        
        #project_text.set(project_text.get().upper())
        #c21 = Checkbutton(window,variable = v21,command = check,wraplength = 60)
        #c21.grid(row = 0,column = 2).
        
       
        
        #e2 = Entry(window,textvariable = customer_text,width = 20)
        #e2.grid(row =1 ,column = 1)
        global mylist 
        mylist = backend.custsearch()
        
        global e2 
        e2 = ttk.Combobox(window,textvariable = customer_text,width = 12)
        
        
        #e2.bind("<Return>", e2_onEnter) #when the enter key is press an event happens  
        #e2.bind('<<ComboboxSelected>>',e2_onEnter)
        
        global mylistc 
        mylistc = backend.custsearch()
        e2['values'] = tuple(mylistc)
        
        
        e2.grid(row =1 ,column = 1,sticky = N)
        global dut_text 
        dut_text= StringVar()
        global e3
        e3 = ttk.Combobox(window,textvariable = dut_text,width = 12)#,values=(1, 2, 4, 8,12,14,16))
        e3.grid(row =2+ x ,column = 1,sticky = N)
        
        global mylistd 
        mylistd = backend.dutsearch()
        e3['values'] = tuple(mylistd)
        global stackup_text 
        stackup_text = StringVar()
        global e4 
        e4 = ttk.Combobox(window,textvariable = stackup_text,width = 12)
        e4.grid(row =3+x ,column = 1,sticky = N)
        global mylists 
        mylists = backend.stacksearch()
        e4['values'] = tuple(mylists)
        
        global TotalIO_text 
        TotalIO_text = StringVar()
        
        global e5 
        e5 = ttk.Combobox(window,textvariable = TotalIO_text,width = 12)
        e5.grid(row =1 ,column = 3,sticky = N)
        global PCBcomp_text 
        PCBcomp_text = StringVar()
        global e6 
        e6 = ttk.Combobox(window,textvariable = PCBcomp_text,width = 10)
        e6.grid(row =12 ,column = 10,sticky = N)
        global Testerconfig_text 
        Testerconfig_text = StringVar()
        global e7 
        e7= ttk.Combobox(window,textvariable = Testerconfig_text,width = 12)
        e7.grid(row =2+x ,column = 3,sticky = N)
        global mylistdtstc 
        mylistdtstc = tuple(backend.testerconfigsearch())
        e7['values'] = ['V93K STH DUT-Scale Interface-WSx8PWR ','QCOM 93K DD','V93K DD','V93K DD PS1600 QCOM configuration','Teradyne U-Flex 12"','Uflex']
        global power_text 
        power_text = StringVar()
        global e8 
        e8 = ttk.Combobox(window,textvariable = power_text,width = 12)
        e8.grid(row =3+x ,column = 3,sticky = N)
        
        
        
        
        
        
        
        global b1 
        # button lists
        b1 = Button(window,text = "View all",width = 12,command = view_command)
        b1.grid(row = 0+x1,column = 6,sticky = N)
        global b2 
        b2 = Button(window,text = "Search entry",width = 12,command = searchf_command)
        b2.grid(row = 1+x1,column = 6,sticky = N)
        global b3 
        b3 = Button(window,text = "Add entry",width = 12,command = add_command)
        b3.grid(row = 2+x1,column = 6,sticky = N)
        global b4 
        b4 = Button(window,text = "Update Selected",width = 12,command = update_command)
        b4.grid(row = 3+x1,column = 6,sticky = N)
        global b5 
        b5= Button(window,text = "Delete Selected",width = 12,command = delete_command)
        b5.grid(row = 4+x1,column = 6,sticky = N)
        global b6 
        b6 = Button(window,text = "Close",width = 12,command = window.destroy)
        b6.grid(row = 5+x1,column = 6,sticky = N)
        
        global b7 
        #------------more button for new page
        b7 = Button(window,text = "Options",width = 12,command = p1_command)
        b7.grid(row = 6+x1,column = 6,sticky = N)
        global b8 
        #------------more button for clearing
        b8 = Button(window,text = "Clear all ",width = 12,command = clear_command)
        b8.grid(row = 7+x1,column = 6,sticky = N)
        
        global l27 
        #b11 = Button(window,text = "Save Files ",width = 12,command = save_list)
        #b11.grid(row = 10,column = 6)
        
        l27 = Label(window,text ="List of Designs")
        l27.grid(row = 0+x2,column =7,columnspan = 12,sticky = N)
        #text entry
        global list1
        list1= Listbox(window,height = 12,width = 80)
        list1.grid(row = 1+x2,column = 7,rowspan = 9,columnspan = 12,sticky = N)
        
        #Part Number Entry
        
        global l41
        l41 = Label(window,text = "Enter the Carlsbad PN")
        l41.grid(row = 12+x3,column =12)
        
        
        global l42
        l42 = Label(window,text = "Manufacturer")
        l42.grid(row = 13+x3,column =12)
        global l43
        l43 = Label(window,text = "Manufacturer_PN")
        l43.grid(row = 14+x3,column =12)
        global l82
        l82 = Label(window,text = "Livermore_PN")
        l82.grid(row = 15+x3,column =12)
        global l83
        l83 = Label(window,text = "Comp_Type")
        l83.grid(row = 16+x3,column =12)
        global l81
        l81 = Label(window,text = "Component Break Down",font=("Helvetica", 12))
        l81.grid(row = 11+x3,column =10)
        global l91
        l91 = Label(window,text = "Part Details",font=("Helvetica", 12))
        l91.grid(row = 11+x3,column =13)
        global cap_select
        cap_select = StringVar(window)
        cap_select.set("Capacitor=") # default value
        
        global l51
        l51 = OptionMenu(window,cap_select, "Capacitor<", "Capacitor>", "Capacitor=" )
        l51.grid(row = 13+x3,column =9,sticky = N)
        global Relay_select
        Relay_select = StringVar(window)
        Relay_select.set("Relays =") # default value
        global l61
        l61 = OptionMenu(window,Relay_select, "Relays <", "Relays >", "Relays =" )
        l61.grid(row = 14+x3,column =9,sticky = N)
        global IC_select
        IC_select = StringVar(window)
        IC_select.set("ICs  =") # default value
        global l71
        l71 = OptionMenu(window,IC_select, "ICs <", "ICs >", "ICs  =" )
        l71.grid(row = 15+x3,column =9,sticky = N)
        global l101
        l101 = Label(window,text = "Click here for link",font=("Helvetica", 12),fg="blue", cursor="hand2")
        l101.grid(row = 16+x3,column =9,sticky = N)
        l101.bind("<Button-1>", callback)
        global part_text
        part_text = StringVar()
        global e41
        e41 = ttk.Combobox(window,textvariable = part_text,width = 10)
        e41.grid(row =12+x3 ,column = 13,sticky = N)
        global partlist 
        partlist = samplebomb.partsearch()
        
        e41["values"] = tuple(partlist)
        global manuf_text
        manuf_text = StringVar()
        global e42
        e42 = ttk.Combobox(window,textvariable = manuf_text,width = 10)
        e42.grid(row =13+x3 ,column = 13,sticky = N)
        global manupn_text
        manupn_text = StringVar()
        global e43
        e43 = ttk.Combobox(window,textvariable = manupn_text,width = 10)
        e43.grid(row =14+x3 ,column = 13,sticky = N)
        global partlistmp 
        partlistmp = samplebomb.partsearchmp()
        
        e43["values"] = tuple(partlistmp)
        global capacitor_text
        capacitor_text = StringVar()
        global e51
        e51 = ttk.Combobox(window,textvariable = capacitor_text,width = 10)
        e51.grid(row =13+x3 ,column = 10,sticky = N)
        
        #caplist = samplebomb.partsearch()
        #e51["values"] = tuple(caplist)
        
        global relay_text
        relay_text = StringVar()
        global e61
        e61 = ttk.Combobox(window,textvariable = relay_text,width = 10)
        e61.grid(row =14+x3 ,column = 10,sticky = N)
        
        #partlist = samplebomb.partsearch()
        #e61["values"] = tuple(partlist)
        global ic_text
        ic_text = StringVar()
        global e71
        e71 = ttk.Combobox(window,textvariable = ic_text,width = 10)
        e71.grid(row =15+x3 ,column = 10,sticky = N)
        global hyper_text
        
        hyper_text = StringVar()
        global e101
        e101 = Entry(window,textvariable = hyper_text,width = 12)
        e101.grid(row =16+x3 ,column = 10,sticky = N)
        
        global lv_text
        lv_text = StringVar()
        global e81
        e81 = ttk.Combobox(window,textvariable = lv_text,width = 10)
        e81.grid(row =15+x3 ,column = 13,sticky = N)
        
        global partlistlv
        partlistlv = samplebomb.partsearchlv()
        e81["values"] = tuple(partlistlv)
        global type_text
        type_text = StringVar()
        global e91
        e91 = ttk.Combobox(window,textvariable = type_text,width = 10)
        e91.grid(row =16+x3 ,column = 13,sticky = N)
        
        #partlist = samplebomb.partsearch()
        #e71["values"] = tuple(partlist)
        
        
        
        #b41 = Button(window,text = "Search Part",width = 12,command = searchpart_command)
        #b41.grid(row = 10,column = 12)
        
        
         
        global c14
        c14 = Checkbutton(window,text = "Select all",variable = v16,command = selectall_command,wraplength = 60)
        c14.grid(row =12+x,column = 6,sticky = N)  
        global c51
        c51 = Checkbutton(window,text = "Export to Excel ",variable = v17,wraplength = 40)
        c51.grid(row =11+x,column = 7,rowspan = 11,sticky = N) 
        global c41
        c41 = Checkbutton(window,text = "Where used ? ",variable = v41,command =treeview_list,wraplength = 60)
        c41.grid(row =9+x,column = 12,rowspan = 9,sticky = N)
        global c49
        c49 = Checkbutton(window,text = "Bom search",variable = v49,command =treeview_list,wraplength = 60)
        c49.grid(row =9+x,column = 9,rowspan = 9,sticky = N)
        global c50
        c50 = Checkbutton(window,text = "Part List",variable = v50,command =treeview_list,wraplength = 60)
        c50.grid(row =9+x,column = 7,rowspan = 11,sticky = N)
        global bx1
        bx1 = Button(window,text = "Add BOM ",width = 12,command = addwindwow)
        bx1.grid(row = 8+x,column = 6,sticky = N)
        global bx2
        bx2 = Button(window,text = "Bom search",width = 12,command = Partextraction)
        bx2.grid(row = 10+x,column = 6,sticky = N) 
        global bx3
        bx2 = Button(window,text = "Delete BOM",width = 12,command = DeleteBOM)
        bx2.grid(row = 11+x,column = 6,sticky = N)         
        
         #global bx1
        #bx1 = Button(window,text = "Sign IN  ",width = 12,command = signin)
        #bx1.grid(row = 9,column = 6)
        
        #scroll bar
        global sb1
        sb1 = Scrollbar(window,orient=VERTICAL)
        sb1.grid(row = 0,column = 14,rowspan = 10,sticky=N+S)
        
        list1.configure(yscrollcommand = sb1.set)
        sb1.configure(command=list1.yview)
        
        list1.bind('<<ListboxSelect>>',get_selected_row)
        
        
        #w = Label(window, image=logo)
                  
                  
                  
        #w.grid(row = 0,column =0)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #b8 = Button(window,text = "Insert BOM",width = 12,command = clear_command)
        #b8.grid(row = 7,column = 6)
              
        # Initialize the counter
        #treeview_list()
        #tree.bind('<ButtonRelease-1>', selectItem)  
        #page only for reading
    elif username == "adminr" and password == "password":
        panel1.destroy()
        #messagebox.showinfo("Login info", "Welcome Admin")
        window.wm_title("PCB Database---Readonly")
        #global path
        #path = "logo.png"
        
        ##Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        #img = ImageTk.PhotoImage(Image.open(path))
        #panel = Label(window, image = img1)
        
        #The Pack geometry manager packs widgets in rows or columns.
        #panel.pack(side = "bottom", fill = "both", expand = "yes")
        panel.grid(row =13,column =0,rowspan = 14,columnspan = 3)        
        
        label_1.destroy()
        label_2.destroy()
        entry_1.destroy()
        entry_2.destroy()
        checkbox.destroy()
        logbtn.destroy()        
        
        global l1
        l1 = Label(window,text ="Project Name",fg="blue", cursor="hand2",font=("Helvetica", 12))
        l1.grid(row = 0,column =0,sticky = N)
        l1.bind("<Button-1>", callback)
        global l2
        l2 = Label(window,text ="Customer")
        l2.grid(row = 1,column =0,sticky = N)
        
        global dut_select
        dut_select = StringVar(window)
        dut_select.set("#_of_DUT_=") # default value
        
        global stackup_select
        stackup_select = StringVar(window)
        stackup_select.set("Stackup_Lay_=") # default value
        
        
        
        global l3
        l3 = OptionMenu(window, dut_select, "#_of_DUT_>", "#_of_DUT_<", "#_of_DUT_=")
        l3.grid(row = 2+x,column =0,sticky = N)
        global l4
        l4 = OptionMenu(window, stackup_select, "Stackup_Lay_>", "Stackup_Lay_<", "Stackup_Lay_=")
        l4.grid(row = 3+x,column =0,sticky = N)
        
        
        global ttio_select
        ttio_select = StringVar(window)
        ttio_select.set("Total_IO_=") # default value
        global l5
        l5 = OptionMenu(window, ttio_select, "Total_IO_<", "Total_IO_>", "Total_IO_=")
        l5.grid(row = 1,column =2,sticky = N)
        
        
        
        global pcb_select
        pcb_select = StringVar(window)
        pcb_select.set("pcb_comp_=") # default value
        
        global l6
        l6 = OptionMenu(window, pcb_select, "pcb_comp_>", "pcb_comp_<", "pcb_comp_=")
        l6.grid(row = 12,column =9,sticky = N)
        global l7
        l7 = Label(window,text ="Tester Configuration")
        l7.grid(row = 2+x,column =2,sticky = N)
        
        
        global powerlayer_select 
        powerlayer_select = StringVar(window)
        powerlayer_select.set("powerlayer_=") # default value
        
        global l8 
        l8 =  OptionMenu(window, powerlayer_select, "powerlayer_>", "powerlayer_<", "powerlayer_=")
        l8.grid(row = 3+x,column =2,sticky = N)
        
        
        #l9 = Label(window,text ="#signal_layer")
        #l9.grid(row = 3,column =2)
        
        #l10 = Label(window,text ="#ground_layer")
        #l10.grid(row = 4,column =2)
        

        
        #Customers =['QUALCOMM','SAMSUNG']
        
        #entry  lists
        global project_text 
        project_text = StringVar()
        #project_text.set(project_text.get().upper())
        global e1 
        global lista
        lista =backend.projsearch()
        
        print(lista)
        #e1["values"] = tuple(mylistp)        
        e1 = AutocompleteEntry(lista, window,width = 20)
        project_text = AutocompleteEntry.var 
        #print(e1("textvariable"))
        #e1 = ttk.Combobox(window,textvariable = project_text,width = 20)
        e1.grid(row =0,column = 1,columnspan = 3)
        global customer_text 
        customer_text = StringVar()        
        
        #project_text.set(project_text.get().upper())
        #c21 = Checkbutton(window,variable = v21,command = check,wraplength = 60)
        #c21.grid(row = 0,column = 2).
        
       
        
        #e2 = Entry(window,textvariable = customer_text,width = 20)
        #e2.grid(row =1 ,column = 1)
        global mylist 
        mylist = backend.custsearch()
        
        global e2 
        e2 = ttk.Combobox(window,textvariable = customer_text,width = 12)
        
        
        #e2.bind("<Return>", e2_onEnter) #when the enter key is press an event happens  
        #e2.bind('<<ComboboxSelected>>',e2_onEnter)
        
        global mylistc 
        mylistc = backend.custsearch()
        e2['values'] = tuple(mylistc)
        
        
        e2.grid(row =1 ,column = 1,sticky = N)
        global dut_text 
        dut_text= StringVar()
        global e3
        e3 = ttk.Combobox(window,textvariable = dut_text,width = 12)#,values=(1, 2, 4, 8,12,14,16))
        e3.grid(row =2+ x ,column = 1,sticky = N)
        
        global mylistd 
        mylistd = backend.dutsearch()
        e3['values'] = tuple(mylistd)
        global stackup_text 
        stackup_text = StringVar()
        global e4 
        e4 = ttk.Combobox(window,textvariable = stackup_text,width = 12)
        e4.grid(row =3+x ,column = 1,sticky = N)
        global mylists 
        mylists = backend.stacksearch()
        e4['values'] = tuple(mylists)
        
        global TotalIO_text 
        TotalIO_text = StringVar()
        
        global e5 
        e5 = ttk.Combobox(window,textvariable = TotalIO_text,width = 12)
        e5.grid(row =1 ,column = 3,sticky = N)
        global PCBcomp_text 
        PCBcomp_text = StringVar()
        global e6 
        e6 = ttk.Combobox(window,textvariable = PCBcomp_text,width = 10)
        e6.grid(row =12 ,column = 10,sticky = N)
        global Testerconfig_text 
        Testerconfig_text = StringVar()
        global e7 
        e7= ttk.Combobox(window,textvariable = Testerconfig_text,width = 12)
        e7.grid(row =2+x ,column = 3,sticky = N)
        global mylistdtstc 
        mylistdtstc = tuple(backend.testerconfigsearch())
        e7['values'] = ['V93K STH DUT-Scale Interface-WSx8PWR ','QCOM 93K DD','V93K DD','V93K DD PS1600 QCOM configuration','Teradyne U-Flex 12"','Uflex']
        global power_text 
        power_text = StringVar()
        global e8 
        e8 = ttk.Combobox(window,textvariable = power_text,width = 12)
        e8.grid(row =3+x ,column = 3,sticky = N)
        
        
        
        
        
        
        
        global b1 
        # button lists
        b1 = Button(window,text = "View all",width = 12,command = view_command)
        b1.grid(row = 0+x1,column = 6,sticky = N)
        global b2 
        b2 = Button(window,text = "Search entry",width = 12,command = searchf_command)
        b2.grid(row = 1+x1,column = 6,sticky = N)
        #global b3 
        #b3 = Button(window,text = "Add entry",width = 12,command = add_command)
        #b3.grid(row = 2+x1,column = 6,sticky = N)
        #global b4 
        #b4 = Button(window,text = "Update Selected",width = 12,command = update_command)
        #b4.grid(row = 3+x1,column = 6,sticky = N)
        #global b5 
        #b5= Button(window,text = "Delete Selected",width = 12,command = delete_command)
        #b5.grid(row = 4+x1,column = 6,sticky = N)
        global b6 
        b6 = Button(window,text = "Close",width = 12,command = window.destroy)
        b6.grid(row = 2+x1,column = 6,sticky = N)
        
        global b7 
        #------------more button for new page
        b7 = Button(window,text = "Options",width = 12,command = p1_command)
        b7.grid(row = 3+x1,column = 6,sticky = N)
        global b8 
        #------------more button for clearing
        b8 = Button(window,text = "Clear all ",width = 12,command = clear_command)
        b8.grid(row = 4+x1,column = 6,sticky = N)
        
        global l27 
        #b11 = Button(window,text = "Save Files ",width = 12,command = save_list)
        #b11.grid(row = 10,column = 6)
        
        l27 = Label(window,text ="List of Designs")
        l27.grid(row = 0+x2,column =7,columnspan = 12,sticky = N)
        #text entry
        global list1
        list1= Listbox(window,height = 12,width = 80)
        list1.grid(row = 1+x2,column = 7,rowspan = 9,columnspan = 12,sticky = N)
        
        #Part Number Entry
        
        global l41
        l41 = Label(window,text = "Enter the Carlsbad PN")
        l41.grid(row = 12+x3,column =12)
        
        
        global l42
        l42 = Label(window,text = "Manufacturer")
        l42.grid(row = 13+x3,column =12)
        global l43
        l43 = Label(window,text = "Manufacturer_PN")
        l43.grid(row = 14+x3,column =12)
        global l82
        l82 = Label(window,text = "Livermore_PN")
        l82.grid(row = 15+x3,column =12)
        global l83
        l83 = Label(window,text = "Comp_Type")
        l83.grid(row = 16+x3,column =12)
        global l81
        l81 = Label(window,text = "Component Break Down",font=("Helvetica", 12))
        l81.grid(row = 11+x3,column =10)
        global l91
        l91 = Label(window,text = "Part Details",font=("Helvetica", 12))
        l91.grid(row = 11+x3,column =13)
        global cap_select
        cap_select = StringVar(window)
        cap_select.set("Capacitor=") # default value
        
        global l51
        l51 = OptionMenu(window,cap_select, "Capacitor<", "Capacitor>", "Capacitor=" )
        l51.grid(row = 13+x3,column =9,sticky = N)
        global Relay_select
        Relay_select = StringVar(window)
        Relay_select.set("Relays =") # default value
        global l61
        l61 = OptionMenu(window,Relay_select, "Relays <", "Relays >", "Relays =" )
        l61.grid(row = 14+x3,column =9,sticky = N)
        global IC_select
        IC_select = StringVar(window)
        IC_select.set("ICs  =") # default value
        global l71
        l71 = OptionMenu(window,IC_select, "ICs <", "ICs >", "ICs  =" )
        l71.grid(row = 15+x3,column =9,sticky = N)
        global l101
        l101 = Label(window,text = "Click here for link",font=("Helvetica", 12),fg="blue", cursor="hand2")
        l101.grid(row = 16+x3,column =9,sticky = N)
        l101.bind("<Button-1>", callback)
        global part_text
        part_text = StringVar()
        global e41
        e41 = ttk.Combobox(window,textvariable = part_text,width = 10)
        e41.grid(row =12+x3 ,column = 13,sticky = N)
        global partlist 
        partlist = samplebomb.partsearch()
        
        e41["values"] = tuple(partlist)
        global manuf_text
        manuf_text = StringVar()
        global e42
        e42 = ttk.Combobox(window,textvariable = manuf_text,width = 10)
        e42.grid(row =13+x3 ,column = 13,sticky = N)
        global manupn_text
        manupn_text = StringVar()
        global e43
        e43 = ttk.Combobox(window,textvariable = manupn_text,width = 10)
        e43.grid(row =14+x3 ,column = 13,sticky = N)
        global partlistmp 
        partlistmp = samplebomb.partsearchmp()
        
        e43["values"] = tuple(partlistmp)
        global capacitor_text
        capacitor_text = StringVar()
        global e51
        e51 = ttk.Combobox(window,textvariable = capacitor_text,width = 10)
        e51.grid(row =13+x3 ,column = 10,sticky = N)
        
        #caplist = samplebomb.partsearch()
        #e51["values"] = tuple(caplist)
        
        global relay_text
        relay_text = StringVar()
        global e61
        e61 = ttk.Combobox(window,textvariable = relay_text,width = 10)
        e61.grid(row =14+x3 ,column = 10,sticky = N)
        
        #partlist = samplebomb.partsearch()
        #e61["values"] = tuple(partlist)
        global ic_text
        ic_text = StringVar()
        global e71
        e71 = ttk.Combobox(window,textvariable = ic_text,width = 10)
        e71.grid(row =15+x3 ,column = 10,sticky = N)
        global hyper_text
        
        hyper_text = StringVar()
        global e101
        e101 = Entry(window,textvariable = hyper_text,width = 12)
        e101.grid(row =16+x3 ,column = 10,sticky = N)
        
        global lv_text
        lv_text = StringVar()
        global e81
        e81 = ttk.Combobox(window,textvariable = lv_text,width = 10)
        e81.grid(row =15+x3 ,column = 13,sticky = N)
        
        global partlistlv
        partlistlv = samplebomb.partsearchlv()
        e81["values"] = tuple(partlistlv)
        global type_text
        type_text = StringVar()
        global e91
        e91 = ttk.Combobox(window,textvariable = type_text,width = 10)
        e91.grid(row =16+x3 ,column = 13,sticky = N)
        
        #partlist = samplebomb.partsearch()
        #e71["values"] = tuple(partlist)
        
        
        
        #b41 = Button(window,text = "Search Part",width = 12,command = searchpart_command)
        #b41.grid(row = 10,column = 12)
        
        
         
        global c14
        c14 = Checkbutton(window,text = "Select all",variable = v16,command = selectall_command,wraplength = 60)
        c14.grid(row =12+x,column = 6,sticky = N)  
        global c51
        c51 = Checkbutton(window,text = "Export to Excel ",variable = v17,wraplength = 40)
        c51.grid(row =11+x,column = 7,rowspan = 11,sticky = N) 
        global c41
        c41 = Checkbutton(window,text = "Where used ? ",variable = v41,command =treeview_list,wraplength = 60)
        c41.grid(row =9+x,column = 12,rowspan = 9,sticky = N)
        global c49
        c49 = Checkbutton(window,text = "Bom search",variable = v49,command =treeview_list,wraplength = 60)
        c49.grid(row =9+x,column = 9,rowspan = 9,sticky = N)
        global c50
        c50 = Checkbutton(window,text = "Part List",variable = v50,command =treeview_list,wraplength = 60)
        c50.grid(row =9+x,column = 7,rowspan = 11,sticky = N)
        #global bx1
        #bx1 = Button(window,text = "Add BOM ",width = 12,command = addwindwow)
        #bx1.grid(row = 8+x,column = 6,sticky = N)
        global bx2
        bx2 = Button(window,text = "Bom search",width = 12,command = Partextraction)
        bx2.grid(row = 5+x,column = 6,sticky = N) 
        #global bx3
        #bx2 = Button(window,text = "Delete BOM",width = 12,command = DeleteBOM)
        #bx2.grid(row = 11+x,column = 6,sticky = N)         
        
         #global bx1
        #bx1 = Button(window,text = "Sign IN  ",width = 12,command = signin)
        #bx1.grid(row = 9,column = 6)
        
        #scroll bar
        global sb1
        sb1 = Scrollbar(window,orient=VERTICAL)
        sb1.grid(row = 0,column = 14,rowspan = 10,sticky=N+S)
        
        list1.configure(yscrollcommand = sb1.set)
        sb1.configure(command=list1.yview)
        
        list1.bind('<<ListboxSelect>>',get_selected_row)        
        
        
        
        
        
        
        
        
    else:
        
        messagebox.showerror("Login error", "Incorrect username")    
    



window = Tk()
x = 0
x1 = 0
x2 = 0
x3 = 0
global search_part
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4= IntVar()
v5 = IntVar()
v6 = IntVar()
v7 = IntVar()
v8 = IntVar()
v9= IntVar()
v10 = IntVar()    
v11 = IntVar()
v12 = IntVar()
v13 = IntVar()
v14= IntVar()
v15 = IntVar()
v21 =IntVar()
v16 =IntVar()
v41 = IntVar()
v49 = IntVar()
v50 = IntVar()
v17 = IntVar()
shape_command()    
dimension_command() 
Electrical_Layer()
cPower_Layer()
Signal_Layer()
ground_command() 
DC_Layer()
totPower_Layer()
PIpo_Layer()
DiffIO_command()
LMG_Layer()
Otherio_Layer()
Totapr_cmd()
tst_temp()
BGA_Dimen()
global selectline
global sel1 
#label lists
window.wm_title("PCB Database-V-8.0")


label_1 = Label(window, text="Username")
label_2 = Label(window, text="Password")
path1 = "logo.png"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path1))
panel1 = Label(window, image = img1)
panel1.grid(row =7,column = 0,columnspan = 5)  

entry_1 = Entry(window,width = 20)
entry_1.bind("<Return>", login_click)
entry_2 = Entry(window, show="*")
entry_2.bind("<Return>", login_click)
label_1.grid(row=0, column=0)
label_2.grid(row=1, column=0)
entry_1.grid(row=0, column=1,columnspan = 3)
entry_2.grid(row=1, column=1,columnspan = 3)

checkbox = Checkbutton(window, text="Keep me logged in")
checkbox.grid(row=5, column=0,padx = 10,pady = 10)

logbtn = Button(window, text="Login",width = 20,command = login_click)
logbtn.grid(row=6, column=1,columnspan = 3,padx = 10,pady= 10)
logbtn.bind("<Return>", login_click)


#print(username, password)



    
window.mainloop()
