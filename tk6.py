from tkinter import *
import tkinter
top=Tk('to pesu chef')
mb=Menubutton(top,text="savory",relief=RAISED)
mb.grid()
mb.menu=Menu(mb,tearoff=0)
mb["menu"]=mb.menu
mayovar=IntVar()
ketchVar=IntVar()
mb.menu.add_checkbutton(label="Bajji")
mb.menu.add_checkbutton(label="Pakoda")
mb.menu.add_checkbutton(label="Pasta")
mb.menu.add_checkbutton(label="Noodles")
top.mainloop()