import tkinter as tk
from tkinter import ttk
app=tk.Tk()
app.title("My App")
app.geometry("500x500")

Scale_Int=tk.IntVar(value=15) #this is the value in First

def TT():
    print(Scale_Int.get())

Slider=ttk.Scale(app,
                 command=lambda value:print(value),
                 length=400,
                 from_=1,
                 to=100,
                 orient='horizontal',
                 variable=Scale_Int,
                )
Slider.pack()




Progress = ttk.Progressbar(app,
                            orient='horizontal',
                            length=400,
                            mode='determinate',                            
                            variable=Scale_Int,
                            )
Progress.pack()




Progress.start()
Butoon=ttk.Button(app,text="Click",command=TT)
Butoon.pack()

app.mainloop()