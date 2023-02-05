from tkinter import *
root = Tk()
root.geometry('500x500')
root.title('Tesla')
root.wm_iconbitmap("tesla.ico")




def click():
    text1="Address "+text_box.get('1.0',END)
    lb1.config(text=str(text1))
  
# variables
name_var=StringVar()

text_box=Text(root,font=('arial 20'))
text_box.place(x=0,y=70,relwidth=0.50,relheight=0.35)

entry=Entry(root,textvariable=name_var, width=50,bd=5,font=('arial 15'),bg='red')
entry.place(x=0,y=10,relwidth=1)

b1 = Button(root, text='Click me', font='calibri 15',command=click,fg="White",bg="red")
b1.place(x=200,y=300)

lb1 = Label(root, text="", font="arial 20 bold")
lb1.place(x=150,y=350)

root.mainloop()
 