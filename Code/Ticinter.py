import tkinter as tk
from tkinter import filedialog

def open_folder_dialog():
    folder_path = filedialog.askdirectory(title="Select a folder")
    if folder_path:
        print("Selected folder:", folder_path)
    else:
        print("No folder selected")

# Create the main window
root = tk.Tk()

# Create a button to trigger the folder dialog
button = tk.Button(root, text="Open Folder Dialog", command=open_folder_dialog)
button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
