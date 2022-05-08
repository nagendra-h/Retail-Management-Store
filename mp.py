from tkinter import*
from tkinter import ttk
from manageemp import MEMP
from empview import VEMP



class EMP:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1140x560+210+130")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="#777B7E")
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
            emp_title=Label(self.root,text="EMPLOYEE DETAILS",font=("times new roman",40,"bold"),fg="#793802",bg="#D0F0C0",bd=4,relief=RIDGE,padx=20).place(x=0,y=0,relwidth=1,height=60)

   #  button MANAGE AND VIEW
            btn_manage=Button(self.root,text="MANAGE EMPLOYEE",command=self.memployee,font=("times new roman",15,"italic"),bg="#7F461B",fg="white",cursor="hand2",bd=3).place(x=340,y=70,height=60,width=210)


            btn_view=Button(self.root,text="view",command=self.vemployee,font=("times new roman",20,"italic"),bg="#7F461B",fg="white",cursor="hand2",bd=3).place(x=640,y=70,height=60,width=210)

##----------MANAGE EMP DETAILS -------
        def  memployee(self):
           self.new_win=Toplevel(self.root)
           self.new_obj=MEMP(self.new_win)

  ##---------VIEWW -------
        def  vemployee(self):
           self.new_win=Toplevel(self.root)
           self.new_obj=VEMP(self.new_win)
         
           
           

      
            


          


if  __name__=="__main__":
     root=Tk()
     obj=EMP(root)
     #obj1=VEMP(root)
     root.mainloop()
