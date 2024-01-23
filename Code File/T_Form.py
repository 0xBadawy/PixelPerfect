import tkinter as tk
from tkinter import colorchooser

def choose_color():
    rgb_color, hex_color = colorchooser.askcolor(title="Choose a color")

    # 'rgb_color' is a tuple in the form (r, g, b), where r, g, and b are in the range 0-255
    print("Chosen color (RGB):", rgb_color ,"hex_color", hex_color)
    print("Chosen color (Hexadecimal):", hex_color)

# Create the main window
root = tk.Tk()
root.title("Color Chooser")

# Create a button to open the color chooser
button = tk.Button(root, text="Choose Color", command=choose_color)
button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
