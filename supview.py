from tkinter import*
from tkinter import ttk,messagebox
from managesup import  MSUP
import  sqlite3
class VSUP:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1140x400+214+298")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="white")
            self.root.focus_force()

            self.var_id=StringVar()
            self.var_name=StringVar()
            
            self.var_mobileno=StringVar()
            

           
            
            view_sup=Frame(self.root,bd=3,relief=RIDGE)
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
                messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)


        def  get_data(self,ev):
            f=self.SupplierTable.focus()
            content=self.SupplierTable.item(f)
            row=content['values']
            #print(row)
            self.var_id.set(row[0])
            self.var_name.set(row[1])
            
            self.var_mobile_no.set(row[2])
            
                   
            

                                                           
root=Tk()
obj=VSUP(root)
root.mainloop()
