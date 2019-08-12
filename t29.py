from tkinter import *
root=Tk()
labelframe=LabelFrame(root,labelanchor='sw',text="thsi is a lebelframe",highlightbackground='red',highlightcolor='yellow')
labelframe.pack(fill="both",expand="yes")
left=Label(labelframe,text="inside the label frame")
left.pack()
right=Label(labelframe,text="newly inside the label frame",bg='red')
right.pack()
mainloop()