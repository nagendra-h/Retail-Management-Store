from tkinter import*
from tkinter import ttk
from managesup import MSUP
#from supview import VSUP
import sqlite3
from PIL import Image,ImageTk


class SUP:
        def    __init__(self,master):
            self.master=master
            self.master.geometry("1140x560+210+130")
            self.master.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.master.config(bg="white")
            self.master.focus_force()



            ##### search frame
     #       searc=LabelFrame(self.master,text="Search Employee",font=("times new roman",10,"bold"),bd=2,relief=RIDGE,bg="white")
       #     searc.place(x=250,y=20,width=600,height=70)


            #########option
         #   cmb_search=ttk.Combobox(searc,values=("select","user_id","name"),state="readonly",justify=CENTER,font=("tgoudy old style",10,"bold"))
           # cmb_search.place(x=10,y=10,width=200,height=30)
            #cmb_search.current(0)

            #txtsearch=Entry(searc,font=("tgoudy old style",15,"bold"),bg="lightyellow").place(x=230,y=10,width=200)

            #btsearch=Button(searc,text="search",font=("tgoudy old style",15,"bold"),bg="lightyellow",fg="black").place(x=440,y=10,height=30,width=100)
#-----------------------TITLE---------------------------------------------
            sup_title=Label(self.master,text="SUPPLIER INFORMATION",font=("times new roman",40,"bold"),fg="green",bd=4,relief=RIDGE,padx=20).place(x=0,y=0,relwidth=1,height=60)

   #  button MANAGE AND VIEW
            btn_manage=Button(self.master,text="MANAGE SUPPLIER",command=self.msupplier,font=("times new roman",10,"italic"),bg="black",fg="orange",cursor="hand2").place(x=340,y=70,height=60,width=210)


            btn_view=Button(self.master,text="vVIEW",command=self.vsupplier,font=("times new roman",10,"italic"),bg="black",fg="orange",cursor="hand2").place(x=640,y=70,height=60,width=210)



            view_i=Frame(self.master,bd=3,relief=RIDGE,bg="white")
            view_i.place(x=190,y=140,width=800,height=400)
            self.Logo=Image.open("images/bg.png")
            self.Logo=self.Logo.resize((700,380),Image.ANTIALIAS)
            self.Logo=ImageTk.PhotoImage(self.Logo)

            LeftMenuLogo=Label(view_i,image=self.Logo)
            LeftMenuLogo.place(x=0,y=0,relwidth=1,height=390) 


##----------MANAGE EMP DETAILS -------
        def  msupplier(self):
           self.new_win=Toplevel(self.master)
           self.new_obj=MSUP(self.new_win)

  ##---------VIEWW -------
        def  vsupplier(self):
           self.new_win=Toplevel(self.master)
           self.new_obj=VSUP(self.new_win)
           
           
         
        
class VSUP:
        def    __init__(self,master):
            self.master=master
            self.master.geometry("1140x400+214+298")
            self.master.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.master.config(bg="white")
            self.master.focus_force()

            self.var_id=StringVar()
            self.var_name=StringVar()
            
            self.var_mobileno=StringVar()
            

           
            
            view_sup=Frame(self.master,bd=3,relief=RIDGE)
            view_sup.place(x=0,y=0,relwidth=1,height=400)

            scrolly=Scrollbar(view_sup,orient=VERTICAL)
            scrollx=Scrollbar(view_sup,orient=HORIZONTAL)


            self.SupplierTable=ttk.Treeview(view_sup,columns=("id","name","mobile_no"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            scrollx.pack(side=BOTTOM,fill=X)
            scrolly.pack(side=RIGHT,fill=Y)
            
            scrollx.config(command=self.SupplierTable.xview)
            scrolly.config(command=self.SupplierTable.yview)
            
            
            
            self.SupplierTable.heading("id",text="ID")
            self.SupplierTable.heading("name",text="NAME")
            
            self.SupplierTable.heading("mobile_no",text="MOBILE NO")
            
            self.SupplierTable["show"]="headings"


            self.SupplierTable.column("id",width=90)
            self.SupplierTable.column("name",width=100)
            
            self.SupplierTable.column("mobile_no",width=100)
            

            self.SupplierTable.pack(fill=BOTH,expand=1)
            self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)
            self.show()

        def show(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("select * from supplier")
                rows=cur.fetchall()
                self.SupplierTable.delete(*self.SupplierTable.get_children())
                for row in rows:
                    self.SupplierTable.insert('',END,values=row)

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.master)


        def  get_data(self,ev):
            f=self.SupplierTable.focus()
            content=self.SupplierTable.item(f)
            row=content['values']
            #print(row)
            self.var_id.set(row[0])
            self.var_name.set(row[1])
            
            self.var_mobile_no.set(row[2])
            
      
            


        


if  __name__=="__main__":
     root=Tk()
     obj=SUP(root)
     root.mainloop()
