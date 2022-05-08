import sqlite3
def create_db():
    con=sqlite3.connect(database=r'student.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(stud_id INTEGER (8) PRIMARY KEY NOT NULL ,name text (255) NOT NULL,dob text(255),mobileno INTEGER(8) NOT NULL,email text(18) NOT NULL,company text(255) NOT NULL,status text(20),password INTEGER(8) NOT NULL)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS admin(user_id INTEGER (8) PRIMARY KEY NOT NULL ,name text (255) NOT NULL,password text(255) NOT NULL)")
    con.commit()

    cur.execute("Insert into admin (user_id,name,password) values(?,?,?)",(1,"admin",111))
    con.commit()

create_db()
