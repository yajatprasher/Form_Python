from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()
root.geometry('1500x1200')
s = ttk.Style()
s.theme_use('classic')

#                           Function for inserting records in database

def insert():
    mycon = mysql.connector.connect(host='localhost', user='root', password='12345', database='info')
    print('Database Connected')
    cur = mycon.cursor()

    rn=0
    rn = rege.get()

    cn = 0
    cn = namee.get()

    # Getting input of class from user
    print(var1.get())
    c = ' '
    if var1.get() == 1:
        c='IX'
    if var1.get() == 2:
        c='X'
    if var1.get() == 3:
        c='XI'
    if var1.get() == 4:
        c='XII'

    # Getting Input of study plan from user

    print(var2.get())
    sp=' '
    if var2.get() == 1:
        sp='Regular'
    if var2.get() == 2:
        sp='Online'

    d = l4.get(l4.curselection())

    # Inserting record in the database

    sql = "INSERT INTO sturec values(%s,%s,%s,%s,%s)"
    val = (rn,cn,c,sp,d)
    cur.execute(sql,val)
    mycon.commit()
    print('Record Inserted')
    disp()
# Function updating old values in thr database

def update():
    mycon = mysql.connector.connect(host='localhost', user='root', password='12345', database='info')
    print('Database Connected')
    cur = mycon.cursor()

    rn = 0
    rn = rege.get()

    cn = 0
    cn = namee.get()

    print(var1.get())
    c = ' '
    if var1.get() == 1:
        c = 'IX'
    if var1.get() == 2:
        c = 'X'
    if var1.get() == 3:
        c = 'XI'
    if var1.get() == 4:
        c = 'XII'

    print(var2.get())
    sp = ' '
    if var2.get() == 1:
        sp = 'Regular'
    if var2.get() == 2:
        sp = 'Online'

    d = l4.get(l4.curselection())

    sql = "update sturec set Candidates_Name=%s, Class=%s, Study_Plan=%s, District=%s where Registration_Number=%s"
    print(sql)
    val = (cn, c, sp, d, rn)
    cur.execute(sql, val)
    mycon.commit()
    print('Record Updated')
    disp()

# Function for searching a record in database [record is shown in form itself using registration number]

def search():
    mycon = mysql.connector.connect(host='localhost', user='root', password='12345', database='info')
    print('Database Connected')
    cur = mycon.cursor()

    rn = 0
    rn = rege.get()
    cur.execute('select * from sturec where Registration_Number='+rn)
    res = cur.fetchone()
    print(res)
    for x in res:
        print (x)
    namee.delete(0,END)
    namee.insert(0,str(res[1]))

    if res[2] == 'IX':
        var1.set(1)
    if res[2] == 'X':
        var1.set(2)
    if res[2] == 'XI':
        var1.set(3)
    if res[2] == 'XII':
        var1.set(4)

    if res[3] == 'Online':
        var2.set(1)
    if res[3] == 'Regular':
        var2.set(2)

    #l4.delete(0,END)
    l4.insert(0,str(res[4]))
    l4.bind(0)

#                             Function for displaying records from database

def disp():
    mycon = mysql.connector.connect(host='localhost', user='root', password='12345', database='info')
    print('Database Connected')
    cur = mycon.cursor()
    cur.execute('select * from sturec')
    res = cur.fetchall()

    trv = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5"), show='headings', height=len(res))
    trv.column("#1", anchor=CENTER)
    trv.heading("#1", text='Registration_Number')
    trv.column("#2", anchor=CENTER)
    trv.heading("#2", text='Candidates_Name')
    trv.column("#3", anchor=CENTER)
    trv.heading("#3", text='Class')
    trv.column("#4", anchor=CENTER)
    trv.heading("#4", text='Study_Plan')
    trv.column("#5", anchor=CENTER)
    trv.heading("#5", text='District')
    for i in res:
        trv.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4]))

    trv.place(x=0, y=400)


#                               Labels displayed in the form

# heading

l1 = Label(root, text='THE GREAT INDIAN SCHOOL', font=('verdana',20, 'bold'))
l1.place(x=0, y=0, width=1350, height=100)

# registration number

reg = Label(root, text='REGISTRATION NUMBER', font=('times new roman','10','bold'))
reg.place(x=10, y=140)
rege = Entry(root)
rege.place(x=300, y=140, width=255, height=20)

# Name entry

name = Label(root, text='CANDIDATES NAME', font=('times new roman','10','bold'))
name.place(x=10, y=170)
namee = Entry(root)
namee.place(x=300, y=170, width=255, height=20)

# Class Entry using radiobutton

var1 = IntVar()
clas = Label(root, text='CLASS', font=('times new roman','10','bold'))
clas.place(x=10, y=200)
c1 = Radiobutton(root, text='IX', variable=var1, value=1)
c1.place(x=300, y=200, width=40, height=20)
c2 = Radiobutton(root, text='X', variable=var1, value=2)
c2.place(x=400, y=200, width=40,height=20)
c3 = Radiobutton(root, text='XI', variable=var1, value=3)
c3.place(x=500, y=200, width=40, height=20)
c4 = Radiobutton(root, text='XII', variable=var1, value=4)
c4.place(x=600, y=200, width=40, height=20)

# Study plan entry using radiobutton

var2 = IntVar()
plan = Label(root, text='STUDY PLAN', font=('times new roman','10','bold'))
plan.place(x=10, y=230)
p1 = Radiobutton(root, text='Regular',variable=var2, value=1)
p1.place(x=300, y=230, height=20)
p2 = Radiobutton(root, text='Online', variable=var2, value=2)
p2.place(x=450, y=230, height=20)

# District entry

state = Label(root, text='DISTRICT', font=('times new roman','10','bold'))
state.place(x=10, y=260,)
l4 = Listbox(root, height=20)
l4.place(x=300, y=260, width=90, height=70)
l4.insert(0, 'Almora')
l4.insert(1, 'Bageshwar')
l4.insert(2, 'Chamoli')
l4.insert(3, 'Champawat')
l4.insert(4, 'Bageshwar')
l4.insert(5, 'Dehradun')
l4.insert(6, 'Haridwar')
l4.insert(7, 'Nanital')
l4.insert(8, 'Pauri Garhwal')
l4.insert(9, 'Pithoragarh')
l4.insert(10, 'Rudraprayag')
l4.insert(11, 'Tehri Garhwal')
l4.insert(12, 'U S Nagar')
l4.insert(13, 'Uttarkashi')

# BUTTONS

# button for insertion

b1 = Button(root, text='Submit', font=('algerian','10','bold'), command=insert)
b1.place(x=100, y=340, width=100, height=20)

# button for updating

b2 = Button(root, text='Update', font=('algerian','10','bold'), command=update)
b2.place(x=300, y=340, width=100, height=20)

# button for searching


b3 = Button(root, text='Search', font=('algerian','10','bold'), command=search)
b3.place(x=500, y=340, width=100, height=20)

#                           For displaying records from database

# mycon = mysql.connector.connect(host='localhost', user='root', password='12345', database='info')
# print('Database Connected')
# cur = mycon.cursor()
# cur.execute('select * from sturec')
# res = cur.fetchall()
#
# trv = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5"), show='headings', height=len(res))
# trv.column("#1", anchor=CENTER)
# trv.heading("#1", text='Registration_Number')
# trv.column("#2", anchor=CENTER)
# trv.heading("#2", text='Candidates_Name')
# trv.column("#3", anchor=CENTER)
# trv.heading("#3", text='Class')
# trv.column("#4", anchor=CENTER)
# trv.heading("#4", text='Study_Plan')
# trv.column("#5", anchor=CENTER)
# trv.heading("#5", text='District')

# for i in res:
#     trv.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4]))
#
# trv.place(x=0, y=400)

root.mainloop()