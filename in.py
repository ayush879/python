from tkinter import *
  
rt = Tk() 
rt.title('Modifying Rows')
rt.geometry('400x400')
lb1 = Label(rt, text = 'Item:').grid(row = 0, column = 3)
entry1 = Entry(rt, justify  = RIGHT).grid(row = 0, column = 6)
lb2 = Label(rt, text = 'Quantity:').grid(row = 0, column = 10)
entry2 = Entry(rt, justify  = RIGHT).grid(row = 0, column = 15)
b = Button(rt, text = 'Insert').grid(row = 0, column = 20)
Lb = Listbox(rt) 
Lb.insert(1, 'Python') 
Lb.insert(2, 'Java') 
Lb.insert(3, 'C++') 
Lb.insert(4, 'Any other') 
Lb.pack() 
rt.mainloop() 