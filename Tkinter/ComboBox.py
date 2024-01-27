import tkinter as tk
from tkinter import ttk
app=tk.Tk()
app.title("My App")
app.geometry("500x500")

item =("Footbal","Basketball","Volleyball")

def test():
    print("Done")
    
    
Item_Drop = tk.StringVar(value=item[0])
compo = ttk.Combobox(app)

compo['values']=item
compo['textvariable']=Item_Drop   # to link the value of the combo box to the variable
compo.pack()


compo.bind("<<ComboboxSelected>>",lambda e:print(compo.get()))  # to get the value of the combo box
compo.bind("<<ComboboxSelected>>",lambda e:print(compo.get()))  # to get the value of the combo box

label = ttk.Label(app,textvariable=Item_Drop)
label.pack()


app.mainloop()