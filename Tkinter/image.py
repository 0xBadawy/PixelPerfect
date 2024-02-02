import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter as ctk
from PIL import Image, ImageDraw, ImageFont


app=tk.Tk()
app.title("My App")
app.geometry("500x500")


# ==================== ttk.Label Image ====================
image_original = Image.open('Test_images/w.jpg').resize((10, 10))
Image_tk = ImageTk.PhotoImage(image_original)

lable_image=ttk.Label(app,text="e",image=Image_tk)
lable_image.pack()

button1 = ttk.Button(app, text="Click Me",image=Image_tk,compound="left")
button1.pack()


# ==================== ctk.CTkImage ====================

img_ctk=ctk.CTkImage(light_image= Image.open('Test_images/w.jpg'),
                     dark_image=Image.open('Test_images/w.jpg')
                    )

button1 = ctk.CTkButton(app, text="Click Me",image=img_ctk,compound="left")
button1.pack()






app.mainloop()
