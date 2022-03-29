class ope:
    def __init__(self):
        self.l1=[]

    def accept(self):
        n=int(input("enter the Number of Elements for n:"))
        for i in range(0,n):
            e=int(input("Enter element: "))
            #if type(e)==str:
             #   print(int(e))
            self.l1.append(e)
            #else:
        #p=self.l1.pop()
        #self.l1.append(str(p))
        
        print("list : ",self.l1)

    def __add__(self,other):
        newlist=[]
        e=input("enter the element for 1")
        w=int(input('enter the elemnet for 2'))
        self.l1.append(e)
        other.l1.append(w)
        for i in range(0,len(self.l1)):
            if type(self.l1[i])==type(other.l1[i]):
                newlist.append(self.l1[i]+other.l1[i])
            else:
                print('type miss match')
        print("After Addition : ",newlist)

    def __sub__(self,other):
        newlist=[]
        for i in range(0,len(self.l1)):
            newlist.append(self.l1[i]-other.l1[i])
        print("After Subtraction: ",newlist)
    
    def __mul__(self,other):
        newlist=[]
        for i in range(0,len(self.l1)):
            newlist.append(self.l1[i]*other.l1[i])
        print("After Multipication: ",newlist)

    def __floordiv__(self,other):
        newlist=[]
        for i in range(0,len(self.l1)):
            newlist.append(self.l1[i]//other.l1[i])
        print("After Floor Division: ",newlist)

    def __gt__(self,other):
        newlist=[]
        for i in range(0,len(self.l1)):
            newlist.append(self.l1[i]>other.l1[i])
        print("After Floor Division: ",newlist)
    
