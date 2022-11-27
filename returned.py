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

def returnsql():
    book_id=returned_id.get()
    rename=rname.get()

    cur.execute("""SELECT* FROM books WHERE bid=?""",(book_id,))
    i=cur.fetchone()
    con.commit()


    try:
        if i==None:
                messagebox.showwarning("ENTER CORRECT ID")

        else:
                print("book can be availed")
                cur.execute("UPDATE books SET status=('avail') WHERE bid=?",(book_id,))
                con.commit()
                cur.execute("INSERT INTO availed (bid,books)VALUES(?,?)",(book_id,rename))
                con.commit()
                print("table updated")
                print("success")
                messagebox.showinfo("book availed")
    except:
                messagebox.showinfo("cant connect to server")
def returned():
    global returned_id,rname
    rewind=Tk()
    rewind.minsize(width="100",height="100")
    img=PhotoImage(file="home.png",master=rewind)
    back_label=Label(rewind,image=img)
    back_label.pack()

    frame_label=Label(rewind,bg="black")
    frame_label.place(relheight=0.5,relwidth=0.5,relx=0.3,rely=0.1)

    bid_label=Label(frame_label,text="Enter book id :",bg="black",fg="white")
    bid_label.place(relheight=0.1,relwidth=0.4,relx=0.1,rely=0.2)

    returned_id=Entry(frame_label,bg="white",fg="black")
    returned_id.place(relheight=0.1,relwidth=0.4,relx=0.4,rely=0.2)

    name_label=Label(frame_label,text="Enter book name: ",bg="black",fg="white")
    name_label.place(relheight=0.1, relwidth=0.4, relx=0.1, rely=0.4)

    rname = Entry(frame_label, bg="white", fg="black")
    rname.place(relheight=0.1, relwidth=0.4, relx=0.4, rely=0.4)

    #buttons

    submit_button=Button(frame_label,bg="white",fg="black",text="SUBMIT",command=returnsql)
    submit_button.place(relheight=0.08,relwidth=0.1,relx=0.3,rely=0.8)

    quit= Button(frame_label, bg="white", fg="black", text="QUIT",command=rewind.destroy)
    quit.place(relheight=0.08, relwidth=0.1, relx=0.5, rely=0.8)



    rewind.mainloop()
