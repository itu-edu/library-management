from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('library_info.db')
cursor = conn.cursor()

def delete_db():
    global id

    bid = id.get()

    print(bid, end='--')
    print("delete")

    try:
        cursor.execute('''DELETE FROM Books WHERE Book_id = ?''', (bid,))
        conn.commit()
        messagebox.showinfo('Success', "Book deleted Successfully")

    except:
        messagebox.showinfo("Error", "Book with given id does not exist")

    window.destroy()


def deleteBooks():
    global id
    global window

    window = Tk()
    window.title('Library Management')
    window.minsize(width=400, height=400)
    window.geometry("600x500")

    headingFrame1 = Frame(window, bg="green", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="Delete Books", fg='black')
    headingLabel.place(relx=0.02, rely=0.1, relwidth=0.96, relheight=0.5)

    # ----------id-------------------

    L = Label(window, font=('arial', 15, 'bold'), text="Enter Book id: ")
    L.place(relx=0.05, rely=0.3)


    id = Entry(window, width=5, font=('arial', 15, 'bold'))
    id.place(relx=0.3, rely=0.3, relwidth=0.62)

    submitbtn = Button(window, text="Submit", command=delete_db, bg="DodgerBlue2", fg="black",
                       font=('arial', 15, 'bold'))
    submitbtn.place(relx=0.05, rely=0.4)

    print("delete")