from tkinter import *
from tkinter import messagebox
import mysql.connector


def issue_db():
    global id
    global StudentName

    bid = id.get()
    bStudentName = StudentName.get()

    # db = mysql.connector.connect(host="localhost", user="root", password='your password', database='db')
    # cursor = db.cursor()

    print(bid, end='--')
    print(bStudentName, end='--')
    print("issue")

    try:
        checkavailability = " select * from books where available='YES';"
        print(checkavailability)
        # cursor.execute(checkavailability)

        flag = 0

        # for i in cursor:
        #     print(i[0])
        #     if (i[0] == bid):
        #         flag = 1
        #         break;

        if flag == 1:
            updatequery = "update books set available='NO' where bid='" + bid + "';"
            print(updatequery)
            # cursor.execute(updatequery)
            # db.commit()

            sqlquery = "insert into issue values('" + bid + "','" + bStudentName + "' );"
            print(sqlquery)

            # cursor.execute(sqlquery)
            # db.commit()

            messagebox.showinfo('Success', "Book issued Successfully")
        else:
            messagebox.showinfo("Error", "Required Book is not available")
    except:
        messagebox.showinfo("Error", "Cannot issue given book ")


def issueBooks():
    global id
    global StudentName

    window = Tk()
    window.title('Library Management')
    window.minsize(width=400, height=400)
    window.geometry("600x500")

    # greet = Label(window, font=('arial', 30, 'bold'), text="Issue Books")
    # greet.grid(row=0, columnspan=3)

    headingFrame1 = Frame(window, bg="green", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="Issue Books", fg='black')
    headingLabel.place(relx=0.02, rely=0.1, relwidth=0.96, relheight=0.5)

    # ----------id-------------------

    L = Label(window, font=('arial', 15, 'bold'), text="Enter Book id: ")
    L.place(relx=0.05, rely=0.3)

    # L = Label(window, font=('arial', 15, 'bold'), text="   ")
    # L.grid(row=2, column=2)

    id = Entry(window, width=5, font=('arial', 15, 'bold'))
    id.place(relx=0.3, rely=0.3, relwidth=0.62)

    # ----------StudentName-------------------

    L = Label(window, font=('arial', 15, 'bold'), text="Enter StudentName: ")
    L.place(relx=0.05, rely=0.5)

    L = Label(window, font=('arial', 15, 'bold'), text="   ")
    L.grid(row=4, column=2)

    StudentName = Entry(window, width=5, font=('arial', 15, 'bold'))
    StudentName.place(relx=0.3, rely=0.5, relwidth=0.62)

    submitbtn = Button(window, text="Submit", command=issue_db, bg="DodgerBlue2", fg="white",
                       font=('arial', 15, 'bold'))
    submitbtn.place(relx=0.3, rely=0.9, relwidth=0.62)

    print("issue")
    pass