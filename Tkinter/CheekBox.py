import tkinter as tk
from tkinter import ttk

app=tk.Tk()
app.title("My App")
app.geometry("500x500")



Cheek_text = tk.BooleanVar()
Cheek_box_bool = Cheek_text.get()
Cheek = ttk.Checkbutton(app,
                        text="Check Box" ,
                        variable=Cheek_text,
                        offvalue=0,    # the value retured if it off
                        onvalue=1,     # the value retured if it on
                        )
Cheek.pack()










app.mainloop()