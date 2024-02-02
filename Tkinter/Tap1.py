import tkinter as tk
from tkinter import ttk

app=tk.Tk()
app.title("My App")
app.geometry("500x500")

def test():
    print("Hello World")

button1 = ttk.Button(app, text="Click Me", command=test)
button1.pack()


noteBook = ttk.Notebook(app, width=200, height=200)
tab1 = ttk.Frame(noteBook,  borderwidth=5)
tab2 = ttk.Frame(noteBook,   borderwidth=5)
tab3 = ttk.Frame(noteBook,   borderwidth=5)



lable1 = ttk.Label(tab1, text="Hello World")
lable1.pack()
button1 = ttk.Button(tab1, text="Click Me t1")
button1.pack()

lable2 = ttk.Label(tab2, text="Hello World")
lable2.pack()
button2 = ttk.Button(tab2, text="Click Met2")
button2.pack()

lable3 = ttk.Label(tab3, text="Hello World")
lable3.pack()
button3 = ttk.Button(tab3, text="Click Me 3")


noteBook.add(tab1, text="Tab 1")
noteBook.add(tab2, text="Tab 2")
noteBook.add(tab3, text="Tab 3")


button3.pack()




noteBook.pack()


app.mainloop()