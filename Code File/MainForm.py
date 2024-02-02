import os

import time
import Main
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import colorchooser
from PIL import Image, ImageDraw, ImageFont
import os




# =================== window setup ===================
ctk.set_appearance_mode("dark") # "dark" or "light"
app = ctk.CTk()
app.title("Demo")
app.geometry("1600x900")
#app.geometry("600x600")
# =================== varables ===================

folder_path = ""
first_image=""
font_color = ""
save_in_same_folder = True

def PP():
    print(folder_path)
    print(first_image)

    
    
def get_first_image_path():
    global folder_path , first_image
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            VV= os.path.join(folder_path, file_name)
            print(VV)
            first_image=VV
            #canvas.bind('<Configure>',show_full_image)

            return      
    return None


# =================== images ===================

def fill_image(event):
    global resized_tk
    canvas_ratio = event.width / event.height
    image_ratio=image_original_R.size[0]/image_original_R.size[1]
    if canvas_ratio > image_ratio: 
        width = int(event.width)
        height = int(width / image_ratio)
    else:
        height = int(event.height)
        width = int(height * image_ratio)
    resized_image = image_original_R.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(int(event.width / 2),int(event.height / 2),anchor = 'center',image = resized_tk)


def show_full_image(event):
    IOI()
    global resized_tk, image_original_R, canvas

    canvas_ratio = event.width / event.height
    image_ratio = image_original_R.size[0] / image_original_R.size[1]

    if canvas_ratio > image_ratio:  # Canvas is wider than the image
        height = int(event.height)
        width = int(height * image_ratio)
    else:
        width = int(event.width)
        height = int(width / image_ratio)

    resized_image = image_original_R.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    canvas.create_image(
        int(event.width / 2),
        int(event.height / 2),
        anchor='center',
        image=resized_tk
    )
    

# =================== functions ===================
def Select_Folder():
    folderpath = ctk.filedialog.askdirectory()
    global folder_path
    folder_path = folderpath
    get_first_image_path()
    
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
TopBar_Frame=ctk.CTkFrame(app,fg_color="#fff")
TopBar_Frame.grid(row=0,column=0,columnspan=16,stick='nsew',pady=5,padx=5)


LeftBar_Frame=ctk.CTkFrame(app,fg_color="#FCE")
LeftBar_Frame.grid(row=1,column=0,rowspan=14,columnspan=2,stick='nsew',pady=5,padx=5)

RightBar_Frame=ctk.CTkFrame(app,fg_color="#FCE")
RightBar_Frame.grid(row=1,column=14,rowspan=14,columnspan=2,stick='nsew',pady=5,padx=5)

MiddleBar_Frame=ctk.CTkFrame(app,fg_color="#FCCCCE")
MiddleBar_Frame.grid(row=1,column=2,rowspan=13,columnspan=12,stick='nsew',pady=5,padx=5)


ButtonBar_Frame=ctk.CTkFrame(app,fg_color="#FCCCCE")
ButtonBar_Frame.grid(row=14,column=2,rowspan=1,columnspan=12,stick='nsew',pady=5,padx=5)




# =================== MiddleBar ===================

image_original_R=""
if first_image == "":
    image_original_R = Image.open('Test_images\\SSR.png')
else:
    image_original_R = Image.open(first_image)
        

def IOI():
    global first_image,image_original_R
    #print("Done : ",first_image)
        
    if first_image == "":
        image_original_R = Image.open('Test_images\\SSR.png')
    else:
        image_original_R = Image.open(first_image)
            
        
#image_original_R = Image.open('Test_images\\SSR.png') 
Image_tk_R = ImageTk.PhotoImage(image_original_R)

canvas=tk.Canvas(MiddleBar_Frame,background="#111",highlightthickness=0,relief='flat',bd=0)
canvas.pack(fill='both',expand=True)
canvas.bind('<Configure>',show_full_image)

# =================== ButtonBar ===================



#----------------- ButtonBar Grid -----------------
ButtonBar_Frame.columnconfigure((0,1,2,3,4),weight=1,uniform='a')
ButtonBar_Frame.rowconfigure(0,weight=1,uniform='a')



SelectFolder_Button = ctk.CTkButton(ButtonBar_Frame, text="Select Folder", command=Select_Folder,font=("cairo", 20))
SelectFolder_Button.grid(row=0, column=2, padx=5, pady=5)


SelectFolder_ButtonIII= ctk.CTkButton(ButtonBar_Frame, text=" Folder", command=get_first_image_path,font=("cairo", 20))
SelectFolder_ButtonIII.grid(row=0, column=1, padx=5, pady=5)



SelectFolder_ButtonII= ctk.CTkButton(ButtonBar_Frame, text=" 8", command=PP,font=("cairo", 20))
SelectFolder_ButtonII.grid(row=0, column=4, padx=5, pady=5)





app.mainloop()



