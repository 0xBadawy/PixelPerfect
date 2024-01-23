import customtkinter
import Main
import time
import os

# =================== window setup ===================
customtkinter.set_appearance_mode("light") # "dark" or "light"
app = customtkinter.CTk()
app.title("CTkSwitch Demo")
app.geometry("1600x800")
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
  
    
# =================== widgets defenation ===================
button = customtkinter.CTkButton(app, text="Open Folder", command=Select_Folder)
button2 = customtkinter.CTkButton(app, text="Open ", command=Create_image)





# =================== widgets ===================
button.grid(row=0, column=0, padx=20, pady=20)
button2.grid(row=2, column=0, padx=30, pady=30)



# =================== main ===================






app.mainloop()




