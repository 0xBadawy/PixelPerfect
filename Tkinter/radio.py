import tkinter as tk
from tkinter import ttk

app=tk.Tk()
app.title("My App")
app.geometry("500x500")


def test():
    print("Done")




raido_var=tk.StringVar()
radio1 = ttk.Radiobutton(
    app,
    text='radio 1',
    value='R 1',
    variable=raido_var,
    command=lambda:print(" - ")       
) 

radio2 = ttk.Radiobutton(
    app,
    text='radio 2',
    value='R 2',
    variable=raido_var,
    command=lambda:print(" + ")       
) 
radio1.pack()
radio2.pack()







app.mainloop()