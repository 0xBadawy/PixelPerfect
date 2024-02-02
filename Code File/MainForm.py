import os
import time
import Main
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import colorchooser
from PIL import Image, ImageDraw, ImageFont




# =================== window setup ===================
ctk.set_appearance_mode("dark") # "dark" or "light"
app = ctk.CTk()
app.title("Demo")
#app.geometry("1600x800")
app.geometry("600x600")
# =================== varables ===================

folder_path = ""
font_color = ""
save_in_same_folder = True



# =================== functions ===================
def Select_Folder():
    folderpath = ctk.filedialog.askdirectory()
    global folder_path
    folder_path = folderpath
    
def choose_color():
    rgb_color, hex_color = colorchooser.askcolor(title="Choose a color")
    global font_color
    font_color = hex_color
    #print("Chosen color (RGB):", rgb_color ,"hex_color", hex_color)

def openImage(path):        
    Io = ctk.CTkImage(light_image=Image.open(path),dark_image=Image.open(path),size=(320, 300))
    i = ctk.CTkLabel(app, text="",image=Io)
    i.grid(row=5, column=5, padx=300, pady=30)

def Create_image():  
    start_time = time.time()    
    print(folder_path)
    Main.add_text_and_frame(folder_path)    
    end_time = time.time()
    elapsed_time = end_time - start_time    
    print(f"Done (Time taken: {elapsed_time} seconds)")
    
def TextInfo():  
   text = textbox.get("0.0", "end")          # Retrieve content from the Text widget
   line_count = text.count('\n')             # Count the number of newline characters
   char_count = len(text) - 1                # Exclude the newline character at the end
   word_count = len(text.split())            # Split the string into words
   print(f"Lines: {line_count}", f"Words: {word_count}", f"Characters: {char_count}", sep="\n")
   
   
# =================== widgets defenation ===================
#button = ctk.CTkButton(frame, text="Open Folder", command=Select_Folder)
button2 = ctk.CTkButton(app, text="Open ", command=Create_image)
button3 = ctk.CTkButton(app, text="TEXT ", command=TextInfo)
textbox = ctk.CTkTextbox(app)
textbox.insert("0.0", "new text to insert")  


# =================== test ===================
def checkbox_event():
    global save_in_same_folder
    if save_in_same_folder:
        save_in_same_folder = False
    else:
        save_in_same_folder = True

check_var = ctk.StringVar(value="on")
checkbox = ctk.CTkCheckBox(app, text="CTkCheckBox", command=checkbox_event,variable=check_var, onvalue="on", offvalue="off")




# e1 =ctk.CTkLabel(app, image=converted_image,width=320, height=300)

#openImage("Test_images/w.jpg")

# =================== widgets ===================
# button.grid(row=3, column=4, padx=20, pady=20)
# button2.grid(row=2, column=0, padx=30, pady=30)
# button3.grid(row=2, column=1, padx=30, pady=30)
# textbox.grid(row=5, column=0, padx=30, pady=30)


frame = ctk.CTkFrame(master=app, fg_color="gray40", bg_color="gray40", border_color="gray40", border_width=0)
frame2 = ctk.CTkFrame(master=app, fg_color="red", bg_color="red", border_color="red", border_width=0)


# #app.grid_columnconfigure(0, weight=1 )
# app.grid_rowconfigure(0, weight=1 )
# #frame.grid(row=0, column=0, padx=0, pady=0, sticky="ew")
# frame2.grid(row=0, column=0, padx=0, pady=0, sticky="ew")




frame.pack(fill="y", expand=True, side="bottom")




# button = ctk.CTkButton(app, text="Open Folder", command=Select_Folder)
# button21 = ctk.CTkButton(app, text="Open Folder", command=Select_Folder)


# button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
# button21.grid(row=0, column=1, padx=20, pady=20, sticky="ew")


# =================== main ===================


app.mainloop()




