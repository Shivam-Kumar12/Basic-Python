from tkinter import*
from tkinter import ttk
# import tkinter as tk
root=Tk()   
root.geometry('600x500+0+0')
root.title('Tesla')
root.wm_iconbitmap("tesla.ico")

title=Label(root,text='Course Details',font=('times new roman', 25 ,'bold'),bg="White",fg="Blue",bd=5,relief=RIDGE) 
title.place(x=0,y=0,relwidth=1)

# name=Entry(root,font=('times new roman', 20 ,'bold'),bd=4,relief=RIDGE,bg="white",fg="red",highlightthickness=3)
# name.place(x=0,y=100,relwidth=1)



name=ttk.Entry(root,font=('times new roman', 20 ,'bold'))
name.place(x=0,y=100,relwidth=1)


btn=Button(root,text="CourseDetail")
btn.place(x=120,y=200,relwidth=0.11,width=200)


root.mainloop()