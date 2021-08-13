from addBook import *
from deleteBook import *
from issueBook import *
from returnBook import *
from viewBook import *


class drawBookModule:
    def __init__(self):
        window = Tk()
        window.title("Manage Books")
        window.minsize(width=400, height=400)
        window.geometry("600x500")

        headingFrame1 = Frame(window, bg="green", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

        headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
        headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

        headingLabel = Label(headingFrame2, text="Welcome! Manage books from this module.", fg='black')
        headingLabel.place(relx=0.02, rely=0.1, relwidth=0.96, relheight=0.5)

        # greet = Label(window, font=('arial', 30, 'bold'), text="Welcome! Manage books from this module.")
        # greet.grid(row=0, columnspan=3)

        addbtn = Button(window, text="Add Books", command=addBooks, bg="DodgerBlue2", fg="black",
                        font=('arial', 15, 'bold'))
        addbtn.place(relx=0.35, rely=0.30, relwidth=0.20, relheight=0.08)

        deletebtn = Button(window, text="Delete Books", command=deleteBooks, bg="DodgerBlue2", fg="black",
                           font=('arial', 15, 'bold'))
        deletebtn.place(relx=0.35, rely=0.40, relwidth=0.20, relheight=0.08)

        issuebtn = Button(window, text="Issue Books", command=issueBooks, bg="DodgerBlue2", fg="black",
                          font=('arial', 15, 'bold'))
        issuebtn.place(relx=0.35, rely=0.50, relwidth=0.20, relheight=0.08)

        returnbtn = Button(window, text="Return Books", command=returnBooks, bg="DodgerBlue2", fg="black",
                           font=('arial', 15, 'bold'))
        returnbtn.place(relx=0.35, rely=0.60, relwidth=0.20, relheight=0.08)

        viewbtn = Button(window, text="View Books", command=viewBooks, bg="DodgerBlue2", fg="black",
                         font=('arial', 15, 'bold'))
        viewbtn.place(relx=0.35, rely=0.70, relwidth=0.20, relheight=0.08)

        greet = Label(window, font=('arial', 15, 'bold'), text="Thank you")
        greet.place(relx=0.35, rely=0.80, relwidth=0.20, relheight=0.08)

        window.mainloop()


def manageBookOperations():
    obj = drawBookModule()
    obj.__init__()
