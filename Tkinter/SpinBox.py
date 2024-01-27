import tkinter as tk
from tkinter import ttk
app=tk.Tk()
app.title("My App")
app.geometry("500x500")

item =("Footbal","Basketball","Volleyball")

def test():
    print("Done")
    
    
#Item_Drop = tk.StringVar(value=item[0])
Spin = ttk.Spinbox(app,)

# Spin['values']=item
# Spin['textvariable']=Item_Drop   # to link the value of the combo box to the variable
Spin['from_']=0
Spin['to']=100

Spin.pack()

Spin.bind('<<Icrement>>',lambda e:print(Spin.get()))  # to get the value of the combo box
Spin.bind('<<Decrement>>',lambda e:print(Spin.get()))  # to get the value of the combo box



app.mainloop()