#TK inter

import tkinter
from tkinter import *

root = tkinter.Tk()
root.title("demo")
root.geometry("600x600")

#label
# label = tkinter.Label(root,text="Hiii").pack()

#button
b = Button(root,text="Subscribe",bg="orange",fg="red")
b.grid(column=1,row=0)


#radio
r1 = Radiobutton(root,text="Python",value=1)
r1.grid(column=2,row=1)
r2 = Radiobutton(root,text="Java",value=2)
r2.grid(column=2,row=2)
r3 = Radiobutton(root,text="SQL",value=3)
r3.grid(column=2,row=3)

#entry
t = Entry(root,width=20)
t.grid(column=3,row=0)




root.mainloop()

