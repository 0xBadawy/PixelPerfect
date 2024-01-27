import tkinter as tk
from tkinter import ttk
app=tk.Tk()
app.title("My App")
app.geometry("500x500")


# pythontutorial.net/tkinter/tkinter-event-binding


def test():
    print("Done")

def get_pos(event):
    print(f'x: {event.x} y: {event.y}')

text = tk.Text(app)
text.pack()

entry= ttk.Entry(app)
entry.pack()

button=ttk.Button(app,text="Button",padding=10,cursor="hand2",command=test)
button.pack()

# ======================== Events =========================

app.bind('<Alt-KeyPress-s>',lambda event : print("Df")) # to bind the event to the app
text.bind('<Alt-KeyPress-a>',lambda event : print("Dsf")) # to bind the event if the text box slected

app.bind('<KeyPress>', lambda event: print(f'a button was pressed ({event.char})'))

entry.bind('<FocusIn>',lambda event : print("Slect"))

app.bind('<Motion>',get_pos)
app.mainloop()