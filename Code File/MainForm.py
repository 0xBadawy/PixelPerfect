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
app.geometry("1600x900")
#app.geometry("600x600")
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

# ==================== Grid ================================
app.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15),weight=1,uniform='a')
app.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14),weight=1,uniform='a')






# =================== main Frames ===================
TopBar=ctk.CTkFrame(app,fg_color="#fff")
TopBar.grid(row=0,column=0,columnspan=16,stick='nsew',pady=5,padx=5)


LeftBar=ctk.CTkFrame(app,fg_color="#FCE")
LeftBar.grid(row=1,column=0,rowspan=14,columnspan=2,stick='nsew',pady=5,padx=5)

RightBar=ctk.CTkFrame(app,fg_color="#FCE")
RightBar.grid(row=1,column=14,rowspan=14,columnspan=2,stick='nsew',pady=5,padx=5)

MiddleBar=ctk.CTkFrame(app,fg_color="#FCCCCE")
MiddleBar.grid(row=1,column=2,rowspan=14,columnspan=12,stick='nsew',pady=5,padx=5)

# =================== main ===================


app.mainloop()




