import sqlite3
from tkinter import *
from tkinter import messagebox

conn = sqlite3.connect('library_info.db')
cursor = conn.cursor()
logged_in_id = 0


def issue_db():
    global id
    global Studentid

    global logged_in_id
    print("issue-id", logged_in_id)

    bid = id.get()
    bStudentId = Studentid.get()
    print("student id to issue book", bStudentId)

    try:
        # get list of all available book, if the one user want to issue
        # is available, user can (update) issue to userid.
        cursor.execute('''SELECT Book_id from Books where Status = 'Available' or Status = 'available' ''')
        result = cursor.fetchall()

        flag = 0

        # if entered bookid belongs to bookid from the available list
        for i in result:
            flag = int(i[0]) == int(bid)
            print("values", i[0], bid, flag, type(bid), type(i[0]))

            if int(i[0]) == int(bid):
                print("to change value of flag check each i", i[0], bid)
                cursor.execute('''UPDATE Books SET Status = ?, User_id = ? WHERE Book_id = ? ''',
                               ("no", int(bStudentId), int(bid)))
                conn.commit()
                messagebox.showinfo('Success', "Book issued Successfully")
                break
            else:
                messagebox.showinfo("Error", "Required Book is not available")
    except:
        messagebox.showinfo("Error", "Cannot issue given book ")

    window.destroy()

def issueBooks():
    global id
    global Studentid
    global window

    window = Tk()
    window.title('Library Management')
    window.minsize(width=400, height=400)
    window.geometry("600x500")

    headingFrame1 = Frame(window, bg="green", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="Issue Books", fg='black')
    headingLabel.place(relx=0.02, rely=0.1, relwidth=0.96, relheight=0.5)

    # ----------id-------------------

    L = Label(window, font=('arial', 15, 'bold'), text="Enter Book id: ")
    L.place(relx=0.05, rely=0.3)


    id = Entry(window, width=5, font=('arial', 15, 'bold'))
    id.place(relx=0.3, rely=0.3, relwidth=0.62)

    # ----------StudentName-------------------

    L = Label(window, font=('arial', 15, 'bold'), text="Enter Student ID: ")
    L.place(relx=0.05, rely=0.5)

    L = Label(window, font=('arial', 15, 'bold'), text="   ")
    L.grid(row=4, column=2)

    Studentid = Entry(window, width=5, font=('arial', 15, 'bold'))
    Studentid.place(relx=0.3, rely=0.5, relwidth=0.62)

    submitbtn = Button(window, text="Submit", command=issue_db, bg="DodgerBlue2", fg="Blue",
                       font=('arial', 15, 'bold'))
    submitbtn.place(relx=0.3, rely=0.9, relwidth=0.62)

    print("issue")