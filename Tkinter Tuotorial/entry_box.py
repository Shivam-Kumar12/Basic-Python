from tkinter import *
root = Tk()
root.geometry('500x500')
root.title('Tesla')
root.wm_iconbitmap("tesla.ico")
Label(root, text="YOUTUBE CHANNEL", font="arial 20 bold").pack()
# lb2=Label(root, text="enter your name:", font="arial 20 bold",)
# lb2.pack(side=TOP)
entry=Entry(root,width=50)
entry.pack()

def click():
    text1="Please Subscribe "+entry.get()
    lb1 = Label(root, text=text1, font="arial 20 bold")
    lb1.pack()


b1 = Button(root, text='Click me', font='calibri 15', command=click,fg="White",bg="red")
b1.pack(padx=50,pady=50)


root.mainloop()
