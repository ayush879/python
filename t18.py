from tkinter import *
import tkinter
top=Tk()
mb=Menubutton(top,text="savory",relief=RAISED)
mb.grid()
mb.menu=Menu(mb,tearoff=0)
mb["menu"]=mb.menu
mayoVar=IntVar()
ketchVar=IntVar()
mb.menu.add_checkbutton(label="bajji",variable=mayoVar)
mb.menu.add_checkbutton(label="pakora",variable=ketchVar)
top.mainloop()