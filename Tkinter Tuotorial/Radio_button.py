from tkinter import*
# import tkinter as tk
root=Tk()   
root.geometry('500x500')
root.title('Tesla')
root.wm_iconbitmap("tesla.ico")

def gender_get():
    print(gender.get())
gender=StringVar()

male=Radiobutton(root,variable=gender,value="Male",text="Male",font="arial 15 bold")
male.place(x=50,y=50)
gender.set('Male')
Female=Radiobutton(root,variable=gender,value="Female",text="Female",font="arial 15 bold")
Female.place(x=200,y=50)
button=Button(root,text="Submit",font="calibri 15 bold",command=gender_get)
button.place(x=150,y=100)

root.mainloop()
 