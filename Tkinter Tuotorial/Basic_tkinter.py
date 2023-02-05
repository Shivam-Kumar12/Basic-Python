from tkinter import*
# import tkinter as tk
# (this is tthe another way to import tkinter but we have to take a refrence bject in root as tk)
root=Tk()   
root.geometry('500x500')
root.title('Tesla')
root.wm_iconbitmap("tesla.ico")
# wm_iconbitmap is used for get an logo
root.resizable(False,False)
# resizable is used to remove/blur he maximize button
root.mainloop()