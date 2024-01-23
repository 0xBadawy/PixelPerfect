import os
import Functions
import datetime
from PIL import Image, ImageDraw, ImageFont

folder_path = "Images"
text_color = (0, 0, 0)
save_in_same_folder = True
automatic_date = True

if(automatic_date):
    today = datetime.date.today()
    T_Year = str(today.year)
    #T_Month value in numbers 
    T_Month = today.strftime("%B")
    T_Month = str(today.month)   
    T_Day = str(today.day)
else:
    T_Year = "2021"
    T_Month = "April"
    T_Day = "10"
    

T_First_line ="First line of text"
T_Second_line = "Second line of text"

texts = [T_Year+T_Month+T_Day, T_First_line, T_Second_line]
text_positions = [(1530, 1220), (960, 1300), (950, 1400)]
text_colors = [(190, 135, 135), (93, 44, 39),  (93, 44, 39)]


image_files = [file for file in os.listdir(folder_path) if file.endswith((".png", ".jpg", ".jpeg"))]

for file in image_files:
    
    image_path = os.path.join(folder_path, file)
    image = Image.open(image_path)


    # ================ Add Frame Image ================
    Frame_image = Image.open("Frame.png").convert("RGBA")                       # To be transparent
    Frame_image = Frame_image.resize((image.width, Frame_image.height))
    Frame_pos = (0, image.height - Frame_image.height)    
    image.paste(Frame_image, Frame_pos, mask=Frame_image)
    
    

    # ================ Add Texts on image ================
    d = ImageDraw.Draw(image)
    font = ImageFont.truetype("Fonts/Cairo-Bold.ttf", 50)
    for text, pos, color in zip(texts, text_positions, text_colors):
        d.text(pos, text=text, font=font, fill=color)
  

    # ================ Create a folder or not to save the modified images ================
    if(save_in_same_folder):
        image.save(os.path.join(folder_path, "modified_" + file))
    else:
        modified_folder_path = os.path.join(folder_path, "Modified_Images")
        os.makedirs(modified_folder_path, exist_ok=True)
        image.save(os.path.join(modified_folder_path, "modified_" + file))
