import tkinter as tk


# Create the main window
window = tk.Tk()
window.title("Demo")
window.geometry("600x900")

# Create a label
label = tk.Label(window, text="Enter your name:")
label.pack()


# Create a text box
text_box = tk.Entry(window)
text_box.pack()

def ty():
    label.config(text="Hello, " + text_box.get())



button=tk.Button(window, text="Click me!", command=ty)
button.pack()

# Run the main window loop
window.mainloop()