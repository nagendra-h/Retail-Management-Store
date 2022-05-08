import sqlite3
def create_db():
    con=sqlite3.connect(database=r'coding.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(user_id INTEGER (8) PRIMARY KEY NOT NULL ,name text (255) NOT NULL,doj text(255),mobileno INTEGER(8) NOT NULL,password INTEGER(8) NOT NULL,utype text(255)NOT NULL)")
    con.commit


    cur.execute("CREATE TABLE IF NOT EXISTS supplier(id INTEGER(8) PRIMARY KEY NOT NULL,name text(255) NOT NULL,mobile_no INTEGER(10)NOT NULL)")
    con.commit()


    cur.execute("CREATE TABLE IF NOT EXISTS  productt(prod_no INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL, category text(255) NOT NULL, id  INTEGER(8) NOT NULL,item_no INTEGER(8) NOT NULL,item_name text(255) NOT NULL,price INTEGER(8) NOT NULL,iqty INTEGER(8) NOT NULL,status text(255) NOT NULL)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS admin(aid INTEGER(8) PRIMARY KEY NOT NULL ,name TEXT(255) NOT NULL,password INTEGER(8)NOT NULL )")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS login(id INTEGER(8)  NOT NULL,name text(255) NOT NULL,time text(255) ,date text(255) NOT NULL,tim text(255))")
    con.commit()

    #cur.execute("CREATE TABLE IF NOT EXISTS logout(id INTEGER(8) PRIMARY KEY NOT NULL,) NOT NULL,date text(255) NOT NULL)")
    #con.commit()


    cur.execute("Insert into admin (aid,name,password) values(?,?,?)",(1,"rama",111))
    con.commit()
    #cur.execute("Insert into admin(aid,name,password) values(?,?,?)",(4,"ram",111))
    #con.commit()

    

    


create_db()    
