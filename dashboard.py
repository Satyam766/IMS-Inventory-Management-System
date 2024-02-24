from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from employee import employeeclass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
import sqlite3
from tkinter import messagebox
import os
import time


class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developer By Satyam Gupta")
        self.root.config(bg="white")
        #====title===
        self.icon_title=PhotoImage(file="img/images/logo1.png")
        
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new romen",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #===btn_title===
        btn_title=Button(self.root,text="Logout",command=self.logout,font=("times new romen",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        
        #===clock===
        self.lbl_clock1=Label(self.root,text="Welcome To Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new romen",10,"bold"),bg="grey",fg="white")
        self.lbl_clock1.place(x=0,y=70,relwidth=1,height=30)
        
        #====Left Menu====
        self.MenuLogo=Image.open("img/images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200))
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)
        
        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        
        self.icon_side=PhotoImage(file="img/images/side.png")
        lbl_menu=Button(LeftMenu,text="Menu",font=("times new romen",18),bg="#009688").pack(side=TOP,fill=X)
        
        lbl_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new romen",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        lbl_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new romen",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        lbl_category=Button(LeftMenu,text="Category",command=self.category,font=("times new romen",20,"bold"),image=self.icon_side,compound=LEFT,padx=5,anchor="w",bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        lbl_products=Button(LeftMenu,text="Products",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new romen",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        lbl_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new romen",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        lbl_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new romen",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        
        #===Content====
        self.lbl_employee=Label(self.root,text="Total Employee\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=('goudy old style',20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[0]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=('goudy old style',20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)
        
        self.lbl_category=Label(self.root,text="Total Category\n[0]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=('goudy old style',20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)
        
        self.lbl_product=Label(self.root,text="Total Product\n[0]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=('goudy old style',20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)
        
        self.lbl_sales=Label(self.root,text="Total Sales\n[0]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=('goudy old style',20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)
        
        #===footer===
        self.lbl_clock=Label(self.root,text="IMS-Inventory Management System | Developer By Satyam Gupta\n For any Technical Issue Contact:7668532249",font=("times new romen",10),bg="grey",fg="white").pack(side=BOTTOM,fill=X)
        
        self.update_content()
#======================================================================

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeclass(self.new_win)    
    
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)    
        
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)    
    
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win) 
        
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)
        
    def update_content(self):
        con =sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            cur.execute('select * from product')
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Product\n [{str(len(product))}]')

            cur.execute('select * from supplier')
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Supplier\n [{str(len(supplier))}]')
            
            cur.execute('select * from category')
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n [{str(len(category))}]')
            
            
            cur.execute('select * from employee')
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employee\n [{str(len(employee))}]')
            
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales\n [{str(bill)}]')
            
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock1.config(text=f"Welcome To Inventory Management System\t\t Date: {str(date_)}\t\t Time:{str(time_)} ")
            self.lbl_clock1.after(200,self.update_content)
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)            
    def logout(self):
        self.root.destroy()
        os.system("python login.py")            
                    
            
if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()
