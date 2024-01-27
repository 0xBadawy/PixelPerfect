import tkinter as tk
from tkinter import ttk

app=tk.Tk()
app.title("My App")
app.geometry("500x500")


def test():
    print("Done")


lable = ttk.Label(app, text="Hello World")
lable.pack()

# to set the value of the lable
lable["text"]="New Text"
lable.config(text="New Text")


# ============= to link lable to text box =================================================================
valuable=tk.StringVar()
valuable=tk.StringVar(value="start value")

lableV = ttk.Label(app, text="Hello World",textvariable=valuable)
lableV.pack()

Tb_1 = ttk.Entry(app,textvariable=valuable)
Tb_1.pack()





app.mainloop()