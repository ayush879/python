from tkinter import *
def change_dropdown(*args):
    print(tkvar.get())
root=Tk()
root.title("tk dropdown example")
mainframe=Frame(root)
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)
mainframe.pack(pady=100,padx=100)
tkvar=StringVar(root)
choices=('pizza','lasagne','fries','fish','potatoe')
tkvar.set('pizza')
popupMenu=OptionMenu(mainframe,tkvar,*choices)
Label(mainframe,text="choose a dish").grid(row=1,column=1)
popupMenu.grid(row=2,column=1)
tkvar.trace('w',change_dropdown)
mainloop()