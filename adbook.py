from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

con=sqlite3.connect("try.db")
cur=con.cursor()



def bookRegister():
    print("ATTEMPTING.")
    nbid = bookInfo1.get()
    ntitle = bookInfo2.get()
    nauthor = bookInfo3.get()
    nstatus = bookInfo4.get()
    nstatus = nstatus.lower()



    cur.execute('''INSERT INTO books (bid,title,author,status)
    VALUES(?,?,?,?)''' , (nbid,ntitle,nauthor,nstatus))
    con.commit()
    messagebox.showinfo('Success', "Book added successfully")


    print(nbid)
    print(ntitle)
    print(nauthor)
    print(nstatus)
    print("command completd")


def addwindow():

    global bookInfo1 ,bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    adbook=Tk()
    adbook.title="AddBooks"
    adbook.minsize(height="100", width="100")
    adbook.maxsize(height="900",width="1550")

    img = PhotoImage(file="home.png", master=adbook)
    img_label = Label(adbook, image=img)
    img_label.pack()

    labelFrame = Frame(adbook, bg='black')
    labelFrame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)
#BUTTONS
    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Title
    lb2 = Label(labelFrame, text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Book Author
    lb3 = Label(labelFrame, text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # Book Status
    lb4 = Label(labelFrame, text="Status(Avail/issued) : ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(labelFrame, text="SUBMIT", bg='white', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.2, rely=0.9, relwidth=0.2, relheight=0.1)

    quitBtn = Button(labelFrame, text="Quit", bg='white', fg='black',command=adbook.destroy)
    quitBtn.place(relx=0.7, rely=0.9, relwidth=0.2, relheight=0.1)

    adbook.mainloop()




