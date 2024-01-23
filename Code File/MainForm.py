import customtkinter
import Main
import time
import os
from PIL import Image, ImageTk

# =================== window setup ===================
customtkinter.set_appearance_mode("light") # "dark" or "light"
app = customtkinter.CTk()
app.title("CTkSwitch Demo")
#app.geometry("1600x800")
app.geometry("600x400")
# =================== varables ===================
folder_path = ""

# =================== functions ===================
def Select_Folder():
    folderpath = customtkinter.filedialog.askdirectory()
    global folder_path
    folder_path = folderpath
                
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
button = customtkinter.CTkButton(app, text="Open Folder", command=Select_Folder)
button2 = customtkinter.CTkButton(app, text="Open ", command=Create_image)
button3 = customtkinter.CTkButton(app, text="TEXT ", command=TextInfo)
textbox = customtkinter.CTkTextbox(app)
textbox.insert("0.0", "new text to insert")  




# =================== widgets ===================
button.grid(row=3, column=4, padx=20, pady=20)
button2.grid(row=2, column=0, padx=30, pady=30)
button3.grid(row=2, column=1, padx=30, pady=30)
textbox.grid(row=5, column=0, padx=30, pady=30)



# =================== main ===================


app.mainloop()




