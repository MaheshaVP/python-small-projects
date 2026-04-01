#TK inter

# import tkinter
# from tkinter import *
# from tkinter import messagebox

# root = tkinter.Tk()
# root.title("demo")
# root.geometry("600x600")

#label
# label = tkinter.Label(root,text="Hiii").pack()

#button
# b = Button(root,text="Subscribe",bg="orange",fg="red")
# b.grid(column=1,row=0)


#radio
# r1 = Radiobutton(root,text="Python",value=1)
# r1.grid(column=2,row=1)
# r2 = Radiobutton(root,text="Java",value=2)
# r2.grid(column=2,row=2)
# r3 = Radiobutton(root,text="SQL",value=3)
# r3.grid(column=2,row=3)

#entry
# t = Entry(root,width=20)
# t.grid(column=3,row=0)

#message
# def Button1():
#     messagebox.showinfo("status","Please click on subscribe")

# b = Button(root,text="Python life",command=Button1)
# b.pack()


# root.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
root = tk.Tk()
root.title("scroll text")
root.geometry("600x600")

#label
ttk.Label(root,text="Python life",background="blue",foreground="white",font=("Times new Roman",15)).grid(row=0,column=1)

#combobox
# n=tk.StringVar()
# course=ttk.Combobox(root,width=25,textvariable=n)
# course["values"]=("python","django","ML")
# course.grid(column=1,row=5)
# course.current()

#scroll text
text1 = scrolledtext.ScrolledText(root,wrap=tk.WORD, width=40, height=10)
text1.grid(column=0,pady=10,padx=10)

text1.focus()

root.mainloop()