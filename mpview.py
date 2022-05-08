
from tkinter import*
from tkinter import ttk,messagebox
from manageemp import  MEMP
import  sqlite3
class VEMP:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1140x400+214+298")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="white")
            self.root.focus_force()

            self.var_user_id=StringVar()
            self.var_name=StringVar()
            self.var_doj=StringVar()
            self.var_mobileno=StringVar()
            self.var_password=StringVar()

            self.var_utype=StringVar()


           
            
            view_emp=Frame(self.root,bd=3,relief=RIDGE)
            view_emp.place(x=0,y=0,relwidth=1,height=400)

            scrolly=Scrollbar(view_emp,orient=VERTICAL)
            scrollx=Scrollbar(view_emp,orient=HORIZONTAL)


            self.EmployeeTable=ttk.Treeview(view_emp,columns=("useri_id","name","doj","mobileno","password","utype"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            scrollx.pack(side=BOTTOM,fill=X)
            scrolly.pack(side=RIGHT,fill=Y)
            
            scrollx.config(command=self.EmployeeTable.xview)
            scrolly.config(command=self.EmployeeTable.yview)
            
            
            
            self.EmployeeTable.heading("useri_id",text="USER_ID")
            self.EmployeeTable.heading("name",text="NAME")
            self.EmployeeTable.heading("doj",text="DOJ")
            self.EmployeeTable.heading("mobileno",text="MOBILE NO")
            self.EmployeeTable.heading("password",text="PASSWORD")
            self.EmployeeTable.heading("utype",text="USER TYPE")



            self.EmployeeTable["show"]="headings"


            self.EmployeeTable.column("useri_id",width=90)
            self.EmployeeTable.column("name",width=100)
            self.EmployeeTable.column("doj",width=100)
            self.EmployeeTable.column("mobileno",width=100)
            self.EmployeeTable.column("password",width=100)
            self.EmployeeTable.column("utype",width=100)

            self.EmployeeTable.pack(fill=BOTH,expand=1)
            self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
            self.show()

        def show(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("select * from employee")
                rows=cur.fetchall()
                self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                for row in rows:
                    self.EmployeeTable.insert('',END,values=row)

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{(str(ex))}",parent=self.root)


        def  get_data(self,ev):
            f=self.EmployeeTable.focus()
            content=self.EmployeeTable.item(f)
            row=content['values']
            #print(row)
            self.var_user_id.set(row[0])
            self.var_name.set(row[1])
            self.var_doj.set(row[2])
            self.var_mobileno.set(row[3])
            self.var_password.set(row[4])
            self.var_utype.set(row[5])
                   
            

                                                           
root=Tk()
obj=VEMP(root)
root.mainloop()

