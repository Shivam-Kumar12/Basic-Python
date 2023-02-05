from tkinter import *
root = Tk()
root.geometry('500x500')
root.title('Tesla')
root.wm_iconbitmap("tesla.ico")


def click():
    lb1 = Label(root, text="Please Subscribe my channel", font="arial 20 bold")
    lb1.pack()


b1 = Button(root, text='Subscribe', font='calibri 15', command=click,fg="White",bg="red")
b1.pack(padx=50,pady=50)


root.mainloop()
