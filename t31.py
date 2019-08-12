from tkinter import *
top=Tk()
L1=Label(top,text="user name")
L1.pack(side=LEFT)
e1=Entry(top,bd=5,justify=RIGHT,selectbackground='red',selectborderwidth=2,selectforeground='white',show='#')
e1.pack(side=RIGHT)
top.mainloop()
