import os
import time
import Main
import Functions
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
app.resizable(False, False)
#app.geometry("600x600")
# =================== varables ===================

folder_path = ""
first_image=""
font_color = ""
save_in_same_folder = True
image_original_R8=f"Test_images\\TY.jpg"
image_original_R=f"Test_images\Screenshot_1.jpg"
logo_Path='Test_images\\SSR.png'
image_number_in_folder=0



# =================== images ===================
    
def get_first_image_path():
    global folder_path , first_image
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            first_image=os.path.join(folder_path, file_name)
            return      
    return None

# =================== functions ===================
def Select_Folder():
    folderpath = ctk.filedialog.askdirectory()
    global folder_path
    folder_path = folderpath
    get_first_image_path()
    count_images_in_folder(folderpath)
    image_label.config(MiddleBar_Frame, image=ImageTK)
       
    
def add_bottom_padding(image_path, padding_height, padding_color):
    original_image = Image.open(image_path)
    original_width, original_height = original_image.size
    new_width = original_width
    new_height = original_height + padding_height
    new_image = Image.new("RGB", (new_width, new_height), padding_color)
    new_image.paste(original_image, (0, 0))
    new_image
    
    
    
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
    
def TextInfo(text):  
  #@ text = textbox.get("0.0", "end")          # Retrieve content from the Text widget
   line_count = text.count('\n')             # Count the number of newline characters
   char_count = len(text) - 1                # Exclude the newline character at the end
   word_count = len(text.split())            # Split the string into words
   print(f"Lines: {line_count}", f"Words: {word_count}", f"Characters: {char_count}", sep="\n")
   
   
def count_images_in_folder(folder_path):
    global image_number_in_folder
    image_count = 0
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_count += 1
    image_number_in_folder= image_count
    print(image_number_in_folder)
    NumberOfImage_lable.config(text=str(image_count))


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

def Place_image():
    global first_image,image_original_R        
    if first_image == "":image_original_R = Image.open('Test_images\\SSR.png')
    else:image_original_R = Image.open(first_image)                 
#Place_image()




Image__=Image.open(image_original_R)
Image_width = Image__.width
Image_height = Image__.height
incW=Image_width/1154
incH=Image_height/770
if incW>1 or incH>1:
    if incW>incH:
        Image_height=Image_height/incW
        Image_width=1154
    else:
        Image_width=Image_width/incH
        Image_height=770        
Image_=Image__.resize((int(Image_width),int(Image_height)))
ImageTK=ImageTk.PhotoImage(Image_)
image_label = ttk.Label(MiddleBar_Frame, image=ImageTK,anchor='center')
image_label.pack(fill='both', expand=True,anchor='center')



def update_image(image_path):
    global image_label, ImageTK
    Image__ = Image.open(image_path)
    Image_width = Image__.width
    Image_height = Image__.height
    incW = Image_width / 1154
    incH = Image_height / 770
    if incW > 1 or incH > 1:
        if incW > incH:
            Image_height = Image_height / incW
            Image_width = 1154
        else:
            Image_width = Image_width / incH
            Image_height = 770
    Image_ = Image__.resize((int(Image_width), int(Image_height)))
    ImageTK = ImageTk.PhotoImage(Image_)
    image_label.configure(image=ImageTK)


# =================== ButtonBar ===================
#----------------- ButtonBar Grid -----------------
ButtonBar_Frame.columnconfigure((0,1,2,3,4),weight=1,uniform='a')
ButtonBar_Frame.rowconfigure(0,weight=1,uniform='a')

SelectFolder_Button = ctk.CTkButton(ButtonBar_Frame, text="Select Folder", command=Select_Folder,font=("cairo", 20))
SelectFolder_Button.grid(row=0, column=2, padx=5, pady=5)

NumberOfImage_lable = ttk.Label(ButtonBar_Frame,text="dd")
NumberOfImage_lable.grid(row=0,column=0,sticky='nsew')






# =================== RightBar ===================
RightBar_Frame.columnconfigure(0,weight=1,uniform='a')
RightBar_Frame.rowconfigure((0,1,2,3,4),weight=1,uniform='a')


Logo_Frame=ctk.CTkFrame(RightBar_Frame,fg_color="#FC222E")
Logo_Frame.grid(row=0, column=0,stick='nsew',pady=5,padx=5)

def select_logo():
    global logo_Path
    logo_path_ = ctk.filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if logo_path_:
        logo_Path = logo_path_
        # Display the selected logo image in the Logo_Canvas or perform any other operations with the logo path
        
def P():
    print("Logo_Frame width",Logo_Frame.winfo_width(),"Logo_Frame height",Logo_Frame.winfo_height())
    

# Image_Logo = ImageTk.PhotoImage(Image.open(logo_Path))
# canvas_Logo = tk.Canvas(Logo_Frame,
#                         width=min(1057, Image_Logo.width()),
#                         height=min(770, Image_Logo.height()),
#                         background="#111",
#                         highlightthickness=0,
#                         relief='flat',
#                         bd=0)
# canvas_Logo.pack(fill='both', expand=True)
# canvas_Logo.create_image(0, 0, anchor="nw", image=Image_Logo)
    

# Image_Logo = ImageTk.PhotoImage(logo_Path)
# canvas_Logo=tk.Canvas(Logo_Frame,
#                  width=min(1057,logo_Path.size[0]),
#                  height=min(770,logo_Path.size[1]),
#                  background="#111",highlightthickness=0,relief='flat',bd=0)
# canvas_Logo.pack(fill='both',expand=True)

def er():
    update_image(first_image)

SelectLogo_Button = ctk.CTkButton(RightBar_Frame, text="Select Logo",command=er,font=("cairo", 20))
SelectLogo_Button.grid(row=1, column=0,sticky='n')


# Image_tk_RLogo = ImageTk.PhotoImage(image_original_R)
# Logo_Canvas=tk.Canvas(Logo_Frame,background="#111",highlightthickness=0,relief='flat',bd=0)

# Logo_Canvas.pack(fill='both',expand=True)
# Logo_Canvas.bind('<Configure>',lambda event: show_full_image(event,logo_Path,Logo_Canvas))



app.mainloop()



# Disply image seqace =>   Select_Folder() -> get_first_image_path() -> Place_image()



'''

raido_var=tk.StringVar()
radio1 = ttk.Radiobutton(
    app,
    text='radio 1',
    value='R 1',
    variable=raido_var,
    command=lambda:print(" - ")       
) 

'''