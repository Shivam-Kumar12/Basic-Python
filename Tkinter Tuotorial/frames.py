from tkinter import*
# import tkinter as tk
# (this is tthe another way to import tkinter but we have to take a refrence bject in root as tk)
root=Tk()   
root.geometry('1530x800+0+0')
root.title('Tesla')
root.wm_iconbitmap("tesla.ico")

# Frame & LabelFrame
frame1=Frame(root,bg='white',bd=5,relief=RIDGE)
frame1.place(x=50,y=50,width=450,height=300)

label_frame=LabelFrame(root,text="Student Infoarmation",font="arial 15 bold",bg='white')
label_frame.place(x=530,y=50,width=450,height=300)

root.mainloop()
