from tkinter import*
from tkinter import ttk,messagebox
import  sqlite3
import os
from PIL import Image,ImageTk

class BILLS:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1350x710+0+0")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="black")
            self.root.focus_force()
            self.my_canvas=Canvas(self.root,width=1350,height=80,bd=1)
            '''self.Lo=Image.open("images/bgg1.jpeg")
            self.Lo=self.Lo.resize((650,40),Image.ANTIALIAS)
            self.Lo=ImageTk.PhotoImage(self.Lo)
            self.my_canvas.create_image(650,40,image=self.Lo)'''
                
            self.my_canvas.place(x=0,y=0)
            self.my_canvas.configure(bg="grey")
            self.my_canvas.create_text(650,40,text="BILL DETAILS",font=("times new roman",30,"bold"),fill="PINK")

            '''self.Lo=Image.open("images/bill1.jpeg")
            self.Lo=self.Lo.resize((1340,710),Image.ANTIALIAS)
            self.Lo=ImageTk.PhotoImage(self.Lo)'''
            
            self.phone_im=Label(self.root,bd=3)#image=self.Lo)
            self.phone_im.place(x=0,y=90,width=1350,height=610)
            
            self.Logo1=Image.open("images/bill1.jpg")
            self.Logo1=self.Logo1.resize((1340,610),Image.ANTIALIAS)
            self.Logo1=ImageTk.PhotoImage(self.Logo1)
            
            self.Logo2=Image.open("images/bill2.jpg")
            self.Logo2=self.Logo2.resize((1340,710),Image.ANTIALIAS)
            self.Logo2=ImageTk.PhotoImage(self.Logo2)
            self.ani()
            
            
            

#-----------------------TITLE---------------------------------------------
            #emp_title=Label(self.root,text="EMPLOYEE DETAILS",font=("times new roman",40,"bold"),fg="#FF2800",bg="#4B3619",bd=4,relief=RIDGE,padx=20).place(x=0,y=0,relwidth=1,height=60)

   #  button MANAGE AND VIEW
            btn_manage=Button(self.root,text="CUSTOMER BILL DETAILS",command=self.mbill,font=("times new roman",13,"italic"),fg="#FF2800",bg="grey",cursor="hand2",bd=5)
            btn_manage.place(x=440,y=70,height=60,width=210)


            
            '''leftmenu=Frame(self.root,bd=0,relief=RIDGE,bg="#4B3619")
            leftmenu.place(x=200,y=150,width=600,height=400)

            self.MenuLogo=Image.open("images/bg.png")
            self.MenuLogo=self.MenuLogo.resize((580,380),Image.ANTIALIAS)
            self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

            LeftMenuLogo=Label(leftmenu,image=self.MenuLogo,bg="#4B3619")
            LeftMenuLogo.pack(side=TOP,fill=BOTH)'''




##----------MANAGE EMP DETAILS -------
        def  mbill(self):
           self.new_win=Toplevel(self.root)
           self.new_obj=bill(self.new_win)
        def ani(self):
                self.im=self.Logo1
                self.Logo1=self.Logo2
                self.Logo2=self.im
                #self.Logo3=self.im
                self.phone_im.config(image=self.im)
                self.phone_im.after(1200,self.ani)
                

  
class bill:
        def    __init__(self,root):
            self.root=root
            self.root.geometry("1350x710+0+0")
            self.root.title("RETAIL MANAGEMENT SYSTEM | BCA STUDENTS")
            self.root.config(bg="#222021")
            self.root.focus_force()

            self.var_bill_no=StringVar()

            self.b_list=[]


            #####TITLES==========
            titile=Label(self.root,text="CUSTOMER BILL DETALS",font=("goudy old style",15,"bold"),bg="#222021",fg="#E4CD05").pack(side=TOP,fill=X,padx=10,pady=20)

            lbl_billno=Label(self.root,text="BILL NO",font=("goudy old style",15,"bold"),bg="#222021",fg="#E4CD05").place(x=50,y=70)


            self.lbl_billno=Entry(self.root,textvariable=self.var_bill_no,font=("goudy old style",15),bg="#222021",fg="#E4CD05")
            self.lbl_billno.place(x=200,y=70,width=200)

            button_search=Button(self.root,text="SEARCH",command=self.search,font=("goudy old style",15,"bold"),cursor="hand2",bg="#222021",fg="#E4CD05").place(x=460,y=70,width=200)

            button_clear=Button(self.root,text="clear",command=self.clear,font=("goudy old style",15,"bold"),cursor="hand2",bg="#222021",fg="#E4CD05").place(x=680,y=70,width=200)

            self.button_clear=Button(self.root,text="back",command=self.cl,font=("goudy old style",15,"bold"),cursor="hand2",bg="#222021",fg="#E4CD05").place(x=890,y=70,width=200)


            bill_frame=Frame(self.root,bd=3,relief=RIDGE)
            bill_frame.place(x=50,y=140,height=330,width=200)


            scrolly=Scrollbar(bill_frame,orient=VERTICAL)
            self.bill_list=Listbox(bill_frame,font=("goudy old style",15,"italic"),bg="#222021",fg="#E4CD05")
            scrolly.pack(side=RIGHT,fill=Y)
            scrolly.config(command=self.bill_list.yview)
            self.bill_list.pack(fill=BOTH,expand=1)
            self.bill_list.bind("<ButtonRelease-1>",self.get_data)



            bl_frame=Frame(self.root,bd=3,relief=RIDGE,bg="#222021")
            bl_frame.place(x=290,y=140,height=530,width=600)

            b_titile=Label(bl_frame,text="BILL AREA",font=("goudy old style",15,"bold"),bg="#222021",fg="#E4CD05").pack(side=TOP,fill=X)

            scrolly=Scrollbar(bl_frame,orient=VERTICAL)
            self.bl_list=Listbox(bl_frame,font=("goudy old style",15,"bold"),bg="#222021",fg="#E4CD05")
            scrolly.pack(side=RIGHT,fill=Y)
            scrolly.config(command=self.bl_list.yview)
            self.bl_list.pack(fill=BOTH,expand=1)



            self.show()

            ######=========

        def show(self):
            del self.b_list[:]
            self.bill_list.delete(0,END)
            for i in os.listdir('bill'):
                if i.split('.')[-1]=='txt':
                    self.bill_list.insert(END,i)
                    self.b_list.append(i.split('.')[0])
        def cl(self):
                self.root.destroy()

        
        def get_data(self,ev):
            index_=self.bill_list.curselection()
            file_name=self.bill_list.get(index_)
            bb=file_name
            self.var_bill_no.set(bb)
            self.bl_list.delete('0',END)
            fp=open(f'bill/{file_name}','r')
            for i in fp:
                self.bl_list.insert(END,i)
            fp.close()

        def search(self):
            if self.var_bill_no.get()=="":
                messagebox.showerror("Error:","Bill no should be requored",parent=self.root)
            else:
                if self.var_bill_no.get() in self.b_list:
                    fp=open(f'bill/{self.var_bill_no.get()}.txt','r')
                    self.bl_list.delete('0',END)
                    for i in fp:
                        self.bl_list.insert(END,i)
                    fp.close()
                else:
                    messagebox.showerror("Error:","Invalid Bill no",parent=self.root)


        def clear(self):
                
            self.show()
            self.var_bill_no.set('')
            self.bl_list.delete('0',END)
                    
            


if  __name__=="__main__":
     root=Tk()
     obj=BILLS(root)
     root.mainloop()


            
