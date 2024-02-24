from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk #pip install pillow
import sqlite3
import time
import os
import tempfile
class billClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developer By Satyam Gupta")
        self.root.config(bg="white")
        self.cart_list=[]
        self.chk_print=0
        
        #====title===
        self.icon_title=PhotoImage(file="img/images/logo1.png")
        
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new romen",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #===btn_title===
        btn_title=Button(self.root,text="Logout",command=self.logout,font=("times new romen",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        
        #===clock===
        self.lbl_clock=Label(self.root,text="Welcome To Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new romen",10,"bold"),bg="grey",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        #====Product Frame======
        
        
        
        ProductFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame.place(x=6,y=110,width=410,height=550)
        
        Product_title=Label(ProductFrame,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        
        #======Product Frame1=====
        self.var_search=StringVar()
        ProductFrame1=Frame(ProductFrame,bd=2,relief=RIDGE,bg="white")
        ProductFrame1.place(x=2,y=42,width=398,height=90)
        
        lbl_search=Label(ProductFrame1,text="Search Product | By Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        
        lbl_search=Label(ProductFrame1,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=5,y=45)
        txt_search=Entry(ProductFrame1,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=128,y=47,width=150,height=22)
        btn_search=Button(ProductFrame1,text="Search",command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)     
        btn_show=Button(ProductFrame1,text="Show All",command=self.show,font=("goudy old style",15),bg="grey",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)     
        
        
        Productframe2=Frame(ProductFrame,bd=3,relief=RIDGE)
        Productframe2.place(x=2,y=140,width=398,height=375)
        
        scrolly=Scrollbar(Productframe2,orient=VERTICAL)
        scrollx=Scrollbar(Productframe2,orient=HORIZONTAL)
        
        self.product_Table=ttk.Treeview(Productframe2,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)
        
        self.product_Table.heading("pid",text="P ID")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="QTY")
        self.product_Table.heading("status",text="Status")
              
        self.product_Table["show"]="headings"
        
        self.product_Table.column("pid",width=40)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("qty",width=40)
        self.product_Table.column("status",width=90)
              
        self.product_Table.pack(expand=1,fill=BOTH)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(ProductFrame,text="Note:'Enter 0 Quantity to remove product from the cart'",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)
        
#====================Customer Frame=========================================================    
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        
        customer_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        customer_Frame.place(x=420,y=110,width=530,height=70)
        
        customer_title=Label(customer_Frame,text="Customer Details",font=("goudy old style",15,),bg="lightgrey").pack(side=TOP,fill=X)
        lbl_name=Label(customer_Frame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(customer_Frame,textvariable=self.var_cname,font=("times new roman",15),bg="lightyellow").place(x=80,y=35,width=180)
        
        lbl_contact=Label(customer_Frame,text="Contact No.",font=("times new roman",15),bg="white").place(x=270,y=35)
        txt_contact=Entry(customer_Frame,textvariable=self.var_contact,font=("times new roman",15),bg="lightyellow").place(x=380,y=35,width=140)
        #========cal Cart framw====================
        cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        cal_Cart_Frame.place(x=420,y=190,width=530,height=360)
        
        #=====Calculator Frame========================
        self.var_cal_input=StringVar()
        
        cal_Frame=Frame(cal_Cart_Frame,bd=9,relief=RIDGE,bg="white")
        cal_Frame.place(x=5,y=10,width=268,height=340)
        
        txt_cal_input=Entry(cal_Frame,textvariable=self.var_cal_input,font=("arial",15,"bold"),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)
        
        btn_7=Button(cal_Frame,text='7',font=('arial',15,'bold'),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor='hand2').grid(row=1,column=0)
        btn_8=Button(cal_Frame,text='8',font=('arial',15,'bold'),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor='hand2').grid(row=1,column=1)
        btn_9=Button(cal_Frame,text='9',font=('arial',15,'bold'),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor='hand2').grid(row=1,column=2)
        btn_Add=Button(cal_Frame,text='+',font=('arial',15,'bold'),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor='hand2').grid(row=1,column=3)
       
        btn_4=Button(cal_Frame,text=4,font=('arial',15,'bold'),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor='hand2').grid(row=2,column=0)
        btn_5=Button(cal_Frame,text=5,font=('arial',15,'bold'),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor='hand2').grid(row=2,column=1)
        btn_6=Button(cal_Frame,text=6,font=('arial',15,'bold'),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor='hand2').grid(row=2,column=2)
        btn_sub=Button(cal_Frame,text='-',font=('arial',15,'bold'),command=lambda:self.get_input('-'),bd=5,width=4,pady=10,cursor='hand2').grid(row=2,column=3)
       
        
        btn_1=Button(cal_Frame,text=1,font=('arial',15,'bold'),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor='hand2').grid(row=3,column=0)
        btn_2=Button(cal_Frame,text=2,font=('arial',15,'bold'),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor='hand2').grid(row=3,column=1)
        btn_3=Button(cal_Frame,text=3,font=('arial',15,'bold'),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor='hand2').grid(row=3,column=2)
        btn_mul=Button(cal_Frame,text='*',font=('arial',15,'bold'),command=lambda:self.get_input('*'),bd=5,width=4,pady=10,cursor='hand2').grid(row=3,column=3)
       
        btn_0=Button(cal_Frame,text=0,font=('arial',15,'bold'),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor='hand2').grid(row=4,column=0)
        btn_c=Button(cal_Frame,text='c',font=('arial',15,'bold'),command=self.clear_cal,bd=5,width=4,pady=15,cursor='hand2').grid(row=4,column=1)
        btn_eq=Button(cal_Frame,text='=',font=('arial',15,'bold'),command=self.perform_cal,bd=5,width=4,pady=15,cursor='hand2').grid(row=4,column=2)
        btn_div=Button(cal_Frame,text='/',font=('arial',15,'bold'),command=lambda:self.get_input('/'),bd=5,width=4,pady=15,cursor='hand2').grid(row=4,column=3)
       
        
        #=====Cart Frame==============================
        cart_frame=Frame(cal_Cart_Frame,bd=3,relief=RIDGE)
        cart_frame.place(x=280,y=8,width=245,height=342)
        self.cart_title=Label(cart_frame,text="All\t Total Product: [0] ",font=("goudy old style",15,),bg="lightgrey")
        self.cart_title.pack(side=TOP,fill=X)
       
        
        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)
        
        self.CartTable=ttk.Treeview(cart_frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)
        
        self.CartTable.heading("pid",text="P ID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="QTY")
       
              
        self.CartTable["show"]="headings"
        
        self.CartTable.column("pid",width=40)
        self.CartTable.column("name",width=90)
        self.CartTable.column("price",width=100)
        self.CartTable.column("qty",width=30)
        
              
        self.CartTable.pack(expand=1,fill=BOTH)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)
        
        #===========Add Cart widgets frame=============
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        self.var_stock=StringVar()
        
        
        Add_cartwidgetsframe=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_cartwidgetsframe.place(x=420,y=550,width=530,height=110)
        
        lbl_p_name=Label(Add_cartwidgetsframe,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_cartwidgetsframe,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)
        
        lbl_p_price=Label(Add_cartwidgetsframe,text="Price Per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_name=Entry(Add_cartwidgetsframe,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)
        
        lbl_p_qty=Label(Add_cartwidgetsframe,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(Add_cartwidgetsframe,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)
               
         
        self.lbl_inStock=Label(Add_cartwidgetsframe,text="In Stock",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)
        
        btn_clear_cart=Button(Add_cartwidgetsframe,text="Clear",command=self.clear_cart,font=("times new roman",15,"bold"),bg="lightgrey",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_Add_cart=Button(Add_cartwidgetsframe,text="Add | Update Cart",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)
        
        #===bill Area======================
        bill_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        bill_frame.place(x=953,y=110,width=410,height=410)
        
        bill_title=Label(bill_frame,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="#f44336",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(bill_frame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        
        self.txt_bill_area=Text(bill_frame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
        
    #==========Bill Button=======================================
        bill_menu_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        bill_menu_frame.place(x=953,y=520,width=410,height=140)
        
        self.lbl_amt=Label(bill_menu_frame,text='Bill Amount\n[0]',font=('goudy old style',15,'bold'),bg='#3f51b5',fg='white')
        self.lbl_amt.place(x=2,y=5,width=120,height=70)
        
        self.lbl_discount=Label(bill_menu_frame,text='Discount\n[5%]',font=('goudy old style',15,'bold'),bg='#8bc34a',fg='white')
        self.lbl_discount.place(x=124,y=5,width=120,height=70)
        
        self.lbl_net_pay=Label(bill_menu_frame,text='Net Pay\n[0]',font=('goudy old style',15,'bold'),bg='#607d8b',fg='white')
        self.lbl_net_pay.place(x=246,y=5,width=160,height=70)
        
        btn_print=Button(bill_menu_frame,text='Print',command=self.print_bill,font=('goudy old style',15,'bold'),bg='lightgreen',fg='white',cursor="hand2")
        btn_print.place(x=2,y=80,width=160,height=50)
        
        btn_clearall=Button(bill_menu_frame,text='Clear All',command=self.clear_all,font=('goudy old style',15,'bold'),bg='grey',fg='white',cursor="hand2")
        btn_clearall.place(x=124,y=80,width=160,height=50)
        
        btn_generate=Button(bill_menu_frame,text='Generate/Save Bill',command=self.generate_bill,font=('goudy old style',15,'bold'),bg='#009688',fg='white',cursor="hand2")
        btn_generate.place(x=246,y=80,width=160,height=50)
        
        #=============footer=====================
        footer=Label(self.root,text="IMS-Inventory Management System | Developed By Satyam Gupta \nFor any Technical Issue Contact: 7668532249 ",font=('times with roman',11),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        
        self.show()
        self.update_date_time()
        #self.bill_top()
#=======================All functio=====================================


    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
     
    def clear_cal(self):
        self.var_cal_input.set('')   
        
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))   
        
    def show(self):
        con =sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            cur.execute("select pid,name,price,qty,status from product where status='Active'")    
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
       
    def search(self):          
        con =sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Select Search By Option",parent=self.root)
            else:
                cur.execute("select pid,name,price,qty,status from product where name LIKE '%"+self.var_search.get()+"%' and status='Active'")       
                rows=cur.fetchall()
                if len(rows)!=0:
                   self.product_Table.delete(*self.product_Table.get_children())
                   for row in rows:
                       self.product_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')
        
    def get_data_cart(self,ev):
        f=self.CartTable.focus()
        content=(self.CartTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_inStock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
            
        
    def add_update_cart(self):
        if self.var_pid.get()=='':
            messagebox.showerror("Error","Please select product from the list",parent=self.root)
        elif self.var_qty.get=='':
            messagebox.showerror("Error","Quantity is Required",parent=self.root)
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror("Error","Invaild Quantity",parent=self.root)    
        else:    
            #price_cal=int(self.var_qty.get())*float(self.var_price.get())    
            #price_cal=float(price_cal)
            price_cal=self.var_price.get()
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]            
           
            #=====update cart========================
            present='no'
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1
            if present=='yes':
                messagebox.askyesno('Confirm',"Present already present \n Do you want to Update | Remove from the cart list",parent=self.root)
                if open==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        #self.cart_list[index_][2]=#price_cal    
                        self.cart_list[index_][3]=self.var_qty.get()
            else:                
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_update() 
 
    def bill_update(self):
        self.bill_amt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amt=self.bill_amt+(float(row[2])*int(row[3]))
            
        self.discount=(self.bill_amt*5)/100
        self.net_pay=self.bill_amt-self.discount
        self.lbl_amt.config(text=f'Bill Amt\n{str(self.bill_amt)}')
        self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')
        self.cart_title.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}] ")
            
    def show_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('',END,values=row)       
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def generate_bill(self):
        if self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error",f"Customer Details are Required",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error",f"Please Add Product to the Cart!!!",parent=self.root)
        else:    
            #====Bill Top====
            self.bill_top()
            #====Bill Middle====
            self.bill_middle()
            #====Bill Bootom====
            self.bill_bottom()
            
            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showerror('Saved','Bill has been generated/save in Backend',parent=self.root)
            self.chk_print=1
            
               
    
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\tXYZ-Inventory 
\t Phone No. 7668532249  , Gwalior-474006
{str("="*47)}
Customer Name : {self.var_cname.get()}
Ph No. : {self.var_contact.get()}
Bill No.:{str(self.invoice)}\t\t Date : {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
Product Name\t\t\tQTY\tPrice
{str("="*47)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)
    
    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*47)}
Bill Amount\t\t\t\tRs.{self.bill_amt}        
Discount\t\t\t\t Rs.{self.discount}
Net Pay\t\t\t\t Rs.{self.net_pay} 
{str("="*47)}     
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)
       
       
    def bill_middle(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            for row in self.cart_list:
                
                pid=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status='Inactive'
                if int(row[3])!=int(row[4]):
                    status='Active'    
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n"+name+"\t\t\t"+row[3]+"\tRs."+price) 
                #======update qty in product======
                
                cur.execute('Update product set qty=?,status=? where pid=?',(
                    qty,
                    status,
                    pid
                ))
                con.commit()
            con.close()
            self.show()    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
               
        
    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_inStock.config(text=f"In Stock ")
        self.var_stock.set('')
    
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.cart_title.config(text=f"Cart \t Total Product: [0] ")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
        
    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome To Inventory Management System\t\t Date: {str(date_)}\t\t Time:{str(time_)} ")
        self.lbl_clock.after(200,self.update_date_time)
            
    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo('Print','Please wait while Printing',parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror('Print','Please generate bill, to print the receipt',parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
            
    def logout(self):
        self.root.destroy()
        os.system("python login.py")        
                 
if __name__=="__main__":
    root=Tk()
    obj=billClass(root)
    root.mainloop()
