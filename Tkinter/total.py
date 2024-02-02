import tkinter as tk
from tkinter import ttk

app=tk.Tk()
app.title("My App")
app.geometry("500x500")

e = True
def test():
    global e
    if e == True:
        lable1.pack_forget()
        e = False
    else:
        lable1.pack()
        e = True
        
lable1 = ttk.Label(app, text="Hello World")
lable1.pack()
button1 = ttk.Button(app, text="Click Me")
button1.pack()

button2 = ttk.Button(app, text="Click Me", command=test)
button2.place(relx=1,rely=1, anchor="se")

app.mainloop()