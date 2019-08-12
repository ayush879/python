from tkinter import *
def sel():
    selection="value="+str(var.get())
    label.config(text=selection)
root=Tk()
var=DoubleVar()
scale=Scale(root,variable=var,troughcolor='red',width=25,orient=HORIZONTAL)
scale.pack(anchor=CENTER)
button=Button(root,text="get scale value",command=sel)
button.pack(anchor=CENTER)
label=Label(root)
label.pack()
root.mainloop()
