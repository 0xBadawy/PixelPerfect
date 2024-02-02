import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter as ctk
from PIL import Image, ImageDraw, ImageFont


app=tk.Tk()
app.title("My App")
app.geometry("500x500")


def fill_image(event):
    global resized_tk
    canvas_ratio = event.width / event.height
    image_ratio=image_original_R.size[0]/image_original_R.size[1]

    if canvas_ratio > image_ratio: # canvas is wider than the image
        width = int(event.width)
        height = int(width / image_ratio)
    else:
        # height = int(event.height)
        # width = int(height * image_ratio)
        height = int(event.height)
        width = int(height * image_ratio)

    resized_image = image_original_R.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(
    int(event.width / 2),
    int(event.height / 2),
    anchor = 'center',
    image = resized_tk)




def show_full_image(event):
    global resized_tk
    canvas_ratio = event.width / event.height
    image_ratio=image_original_R.size[0]/image_original_R.size[1]

    # get coordinates
    if canvas_ratio > image_ratio: # canvas is wider than the image
        height = int(event.height)
        width = int(height * image_ratio)
    else: # canvas is narrower than the image
        width = int(event.width)
        height = int(event.height)

    resized_image = image_original_R.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas. create_image(
    int(event.width / 2),
    int(event.height / 2),
    anchor = 'center',
    image = resized_tk)


app.columnconfigure((0,1,2,3),weight=1,uniform='a')
app.rowconfigure(0,weight=1)



# ==================== ttk.Label Image ====================


image_original = Image.open('Test_images/w.jpg').resize((30, 30))
Image_tk = ImageTk.PhotoImage(image_original)

lable_image=ttk.Label(app,text="e",image=Image_tk)
lable_image.grid(row=0,column=0,pady=10)

button1 = ttk.Button(app, text="Click Me",image=Image_tk,compound="left")
button1.grid(row=0,column=0,stick='w')


# ==================== ctk.CTkImage ====================

img_ctk=ctk.CTkImage(light_image= Image.open('Test_images/w.jpg'),dark_image=Image.open('Test_images/w.jpg'))
button1 = ctk.CTkButton(app, text="Click Me",image=img_ctk,compound="left")
button1.grid(row=0,column=0,stick='n')



#+++++++++++++++++++++++======+++++++++++++++++++++++

image_original_R = Image.open('Test_images\TY.jpg') 
Image_tk_R = ImageTk.PhotoImage(image_original_R)

canvas=tk.Canvas(app,background="red")
canvas.grid(column=1,columnspan=3,row=0,sticky='nsew')
canvas.bind('<Configure>',show_full_image)


 

app.mainloop()
