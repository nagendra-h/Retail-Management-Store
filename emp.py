from tkinter import*
from tkinter import ttk
from manageemp import MEMP
import sqlite3
from PIL import Image,ImageTk
#from empview import VEMP



class EMP:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1140x560+210+130")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="orange")
            self.root.focus_force()



            #search frame#
            #searc=LabelFrame(self.root,text="Search Employee",font=("times new roman",10,"bold"),bd=2,relief=RIDGE,bg="white")
          # searc.place(x=250,y=20,width=600,height=70)


            #########option
         #   cmb_search=ttk.Combobox(searc,values=("select","user_id","name"),state="readonly",justify=CENTER,font=("tgoudy old style",10,"bold"))
           # cmb_search.place(x=10,y=10,width=200,height=30)
            #cmb_search.current(0)

            #txtsearch=Entry(searc,font=("tgoudy old style",15,"bold"),bg="lightyellow").place(x=230,y=10,width=200)

            #btsearch=Button(searc,text="search",font=("tgoudy old style",15,"bold"),bg="lightyellow",fg="black").place(x=440,y=10,height=30,width=100)
#-----------------------TITLE---------------------------------------------
            emp_title=Label(self.root,text="EMPLOYEE DETAILS",font=("times new roman",40,"bold"),fg="green",bd=4,relief=RIDGE,padx=20).place(x=0,y=0,relwidth=1,height=60)

   #  button MANAGE AND VIEW
            btn_manage=Button(self.root,text="MANAGE EMPLOYEE",command=self.memployee,font=("times new roman",10,"italic"),bg="black",fg="orange",cursor="hand2").place(x=340,y=70,height=60,width=210)


            btn_view=Button(self.root,text="view",command=self.vemployee,font=("times new roman",10,"italic"),bg="black",fg="orange",cursor="hand2").place(x=640,y=70,height=60,width=210)

############# IMAGE+++++++++++=

            view_i=Frame(self.root,bd=3,relief=RIDGE,bg="white")
            view_i.place(x=230,y=140,width=600,height=400)


            self.Logo=Image.open("images/im1.png")
            self.Logo=self.Logo.resize((400,600),Image.ANTIALIAS)
            self.Logo=ImageTk.PhotoImage(self.Logo)

            LeftMenuLogo=Label(view_i,image=self.Logo)
            LeftMenuLogo.place(x=0,y=0,relwidth=1,height=390) 

##----------MANAGE EMP DETAILS -------
        def  memployee(self):
           self.new_win=Toplevel(self.root)
           self.new_obj=MEMP(self.new_win)

  ##---------VIEWW -------
        def  vemployee(self):
           self.new_win=Toplevel(self.root)
           self.new_obj=VEMP(self.new_win)
         
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
                              
           

      
            


          


if  __name__=="__main__":
     root=Tk()
     obj=EMP(root)
     #obj1=VEMP(root)
     root.mainloop()
