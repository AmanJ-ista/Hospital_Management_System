from tkinter import *
import mysql.connector
from tkinter import messagebox
def appointment():
    global window5
    window5=Tk()
    window5.geometry('1800x1200') 
    window5.title("Hospital Management System")
    frame2=Frame(window5,width=1600,height=54,bg="violet")
    frame2.place(x=0,y=0)
    lb=Label(window5,text="MANAGE APPOINTMENT",bg="violet",font=('calibre',30,'bold'))
    lb.place(x=615,y=0)

    lg=Label(window5,text="DOCTOR NAME",font=('calibre',20,'bold'))
    lg.place(x=280,y=200)
    
    lh=Label(window5,text="PATIENT NAME",font=('calibre',20,'bold'))
    lh.place(x=280,y=250)

    li=Label(window5,text="DATE",font=('calibre',20,'bold'))
    li.place(x=280,y=300)

    lj=Label(window5,text="TIME",font=('calibre',20,'bold'))
    lj.place(x=280,y=350)

    lk=Label(window5,text="SEARCH",font=('calibre',20,'bold'))
    lk.place(x=1200,y=200)


    global e1,e2,e3,ei,ek
    global search,doctor,patient,date,time
    doctor=StringVar()
    patient=StringVar()
    date=StringVar()
    time=StringVar()
    search=StringVar()
    e1=Entry(window5,textvar="doctor",width=20,font=('calibre',18,'bold'))
    e1.place(x=550,y=200)

    e2=Entry(window5,textvar="patient",width=20,font=('calibre',18,'bold'))
    e2.place(x=550,y=250)

    e3=Entry(window5,textvar="date",width=20,font=('calibre',18,'bold'))
    e3.place(x=550,y=300)

    ei=Entry(window5,textvar="time",width=20,font=('calibre',18,'bold'))
    ei.place(x=550,y=350)

    ek=Entry(window5,textvar="search",width=20,font=('calibre',18,'bold'))
    ek.place(x=900,y=200)



    
    bf=Button(window5,text="BACK",bg="orange",font=('calibre',18,'bold'),width=15,command=back)
    bf.place(x=0,y=1)

    bg=Button(window5,text="SUBMIT",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=appointment1)
    bg.place(x=300,y=500)

    bh=Button(window5,text="DELETE",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=delete)
    bh.place(x=530,y=500)

    bi=Button(window5,text="SEARCH",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=bitch)
    bi.place(x=760,y=500)

    bj=Button(window5,text="VIEW",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=show)
    bj.place(x=990,y=500)


def back():
    window5.destroy()


def appointment1():
      
    a=e1.get()
    b=e2.get()
    c=e3.get()
    d=ei.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    sql="INSERT INTO appointment(doctor,patient,date,time)VALUES(%s,%s,%s,%s)"
    val=(a,b,c,d)
    cs.execute(sql,val)
    conn.commit()
    cs.close()
    conn.close()
    e1.delete(first=0,last=20)
    e2.delete(first=0,last=20)
    e3.delete(first=0,last=20)
    ei.delete(first=0,last=20) 

def show():
    window6=Tk()
    window6.geometry('1800x1200')
    tree=ttk.Treeview(window6,column=(1,2,3,4),show="headings",height=30)
    tree.heading(1,text="Doctor")
    tree.heading(2,text="Patient")
    tree.heading(3,text="Date")
    tree.heading(4,text="Time")
    tree.place(x=400,y=100)
    frame2=Frame(window6,width=1600,height=54,bg="violet")
    frame2.place(x=0,y=0)
    lb=Label(window6,text="List Of Appointments",bg="violet",font=('calibre',30,'bold'))
    lb.place(x=615,y=0)


    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    cs.execute("SELECT * FROM appointment")
    rows=cs.fetchall()
    for x in rows:
        tree.insert('','end',values=x)
        

def delete():
    messagebox.askquestion("Confirmation","Are you sure want to delete?")
    b=e2.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    sql="DELETE FROM appointment WHERE patient=%s"
    val=(b,)
    cs.execute(sql,val)     
    conn.commit()
    cs.close()
    conn.close()         

def bitch():
    messagebox.askquestion("Confirmation","Are you sure want to search?")
    z=ek.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="mysql",db="Hospital")
    cs=conn.cursor()
    sql="SELECT * FROM appointment WHERE patient=%s "
    val=(z,)
    cs.execute(sql,val)
    rows=cs.fetchall()
    for x in rows:
        p=x[0]
        q=x[1]
        r=x[2]
        s=x[3]
    if z==q:
        e1.insert(0,p)
        e2.insert(0,q)
        e3.insert(0,r)
        ei.insert(0,s)





