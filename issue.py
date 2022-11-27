from tkinter import*
from PIL import ImageTk,Image
from tkinter import *
from PIL import ImageTk
#Create SQlite database
import sqlite3
import adbook
import view
from tkinter import messagebox



con=sqlite3.connect("try.db")
cur=con.cursor()

def issuesql():
    book_id=issued_id.get()
    sname=name.get()

    cur.execute("""SELECT* FROM books WHERE bid=?""",(book_id,))
    i=cur.fetchone()
    con.commit()


    try:
        if i==None:
                messagebox.showwarning("ENTER CORRECT ID")
        elif i[3]=="issued":
                messagebox.showwarning("Book is unavailable at the moment")
                print("Book is unavailable at the moment")
        else:
                print("book can be issued")
                cur.execute("UPDATE books SET status=('issued') WHERE bid=?",(book_id,))
                con.commit()
                cur.execute("INSERT INTO issued (bid,issuedto)VALUES(?,?)",(book_id,sname))
                con.commit()
                print("table updated")
                print("success")
                messagebox.showinfo("book issued")
    except:
        messagebox.showinfo("cant connect to server")
def issue():
    global issued_id,name
    iswind=Tk()
    iswind.minsize(width="100",height="100")
    img=PhotoImage(file="home.png",master=iswind)
    back_label=Label(iswind,image=img)
    back_label.pack()

    frame_label=Label(iswind,bg="black")
    frame_label.place(relheight=0.5,relwidth=0.5,relx=0.3,rely=0.1)

    bid_label=Label(frame_label,text="Enter book id :",bg="black",fg="white")
    bid_label.place(relheight=0.1,relwidth=0.4,relx=0.1,rely=0.2)

    issued_id=Entry(frame_label,bg="white",fg="black")
    issued_id.place(relheight=0.1,relwidth=0.4,relx=0.4,rely=0.2)

    name_label=Label(frame_label,text="Enter reciever name: ",bg="black",fg="white")
    name_label.place(relheight=0.1, relwidth=0.4, relx=0.1, rely=0.4)

    name = Entry(frame_label, bg="white", fg="black")
    name.place(relheight=0.1, relwidth=0.4, relx=0.4, rely=0.4)

    #buttons

    submit_button=Button(frame_label,bg="white",fg="black",text="SUBMIT",command=issuesql)
    submit_button.place(relheight=0.08,relwidth=0.1,relx=0.3,rely=0.8)

    quit= Button(frame_label, bg="white", fg="black", text="QUIT",command=iswind.destroy)
    quit.place(relheight=0.08, relwidth=0.1, relx=0.5, rely=0.8)



    iswind.mainloop()
