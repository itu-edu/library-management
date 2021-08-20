from addBook import *
from deleteBook import *
from issueBook import *
from returnBook import *
from viewBook import *

class drawBookModule:
    def __init__(self):
        window = Tk()
        window.title("Library Management System - Dashboard")
        window.minsize(width=400, height=400)
        window.geometry("600x500")

        headingFrame1 = Frame(window, bg="green", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

        headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
        headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

        headingLabel = Label(headingFrame2, text="Welcome, User!", fg='black')
        headingLabel.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.5)

        addbtn = Button(window, text="Add New Book", command=addBooks, bg="#455A64", fg="blue")
        addbtn.place(relx=0.35, rely=0.30, relwidth=0.30, relheight=0.08)

        deletebtn = Button(window, text="Delete a Book", command=deleteBooks, bg="#455A64", fg="blue")
        deletebtn.place(relx=0.35, rely=0.40, relwidth=0.30, relheight=0.08)

        issuebtn = Button(window, text="Issue a Book", command=issueBooks, bg="#455A64", fg="blue")
        issuebtn.place(relx=0.35, rely=0.50, relwidth=0.30, relheight=0.08)

        returnbtn = Button(window, text="Return Book", command=returnBooks, bg="#455A64", fg="blue")
        returnbtn.place(relx=0.35, rely=0.60, relwidth=0.30, relheight=0.08)

        viewbtn = Button(window, text="List of Books", command=viewBooks, bg="#455A64", fg="blue")
        viewbtn.place(relx=0.35, rely=0.70, relwidth=0.30, relheight=0.08)

        greet = Label(window, font=('arial', 13, 'bold'), text="Thank you")
        #greet.place(relx=0.35, rely=0.90, relwidth=0.30, relheight=0.08)

        window.mainloop()


def manageBookOperations():
    obj = drawBookModule()
