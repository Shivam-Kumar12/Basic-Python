from tkinter import*
# import tkinter as tk
root=Tk()   
root.geometry('500x500')
root.title('Tesla')
root.wm_iconbitmap("tesla.ico")

def check_get():
    print(check_var.get())

                          # (with INT)
# check_var=IntVar()
# check_btn=Checkbutton(root,variable=check_var,onvalue=1,offvalue=0,text="I agree with your terms and condition",font="arial 15 bold")
# check_btn.place(x=50,y=50)
# check_var.set('0')

# btn=Button(root,text="Submit",font="calibri 15 bold",command=check_get)
# btn.place(x=180,y=100)
check_var=StringVar()
check_btn=Checkbutton(root,variable=check_var,onvalue="on",offvalue="off",text="I agree with your terms and condition",font="arial 15 bold")
check_btn.place(x=50,y=50)
check_var.set('0')

btn=Button(root,text="Submit",font="calibri 15 bold",command=check_get)
btn.place(x=180,y=100)

root.mainloop()
 