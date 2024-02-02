import tkinter as tk
from tkinter import ttk

app=tk.Tk()
app.title("My App")
app.geometry("500x500")


def test():
    print("Done")
    
    
    
frame =  ttk.Frame(app, width=200, height=200, relief=tk.RIDGE, borderwidth=5)
frame.pack_propagate(False) # Prevent frame to shrink
frame.pack()

lable1 = ttk.Label(frame, text="Hello World")
lable1.pack()

button1 = ttk.Button(frame, text="Click Me", command=test)
button1.pack()

lable2 = ttk.Label(app, text="Hello World")
lable2.pack()


app.mainloop()