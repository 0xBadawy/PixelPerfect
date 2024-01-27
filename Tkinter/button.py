import tkinter as tk
from tkinter import ttk

app=tk.Tk()
app.title("My App")
app.geometry("500x500")


def test():
    print("Done")





button=ttk.Button(app,text="Button",padding=10,cursor="hand2",width=20,style="",takefocus=1,command=test) 
button.pack()

# to git the value of the button
value=button["text"]

# to set the value of the button
button["text"]="New Text"

# to disable the button
button["state"]="disabled"
button.config(state="disabled")

# to enable the button
button["state"]="normal"
button.config(state="normal")

# to change the button style
button["style"]="TButton"
button.config(style="TButton")










app.mainloop()