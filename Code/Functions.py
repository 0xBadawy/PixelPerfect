from PIL import Image, ImageOps

def add_bottom_padding_a(image_path, padding_height, padding_color):
    original_image = Image.open(image_path)
    original_width, original_height = original_image.size
    new_width = original_width
    new_height = original_height + padding_height
    new_image = Image.new("RGB", (new_width, new_height), padding_color)
    new_image.paste(original_image, (0, 0))
    new_image.show()

def add_bottom_padding(image_path, padding_height, padding_color):
    original_image = Image.open(image_path)
    original_width, original_height = original_image.size
    new_width = original_width
    new_height = original_height + padding_height
    new_image = Image.new("RGB", (new_width, new_height), padding_color)
    new_image.paste(original_image, (0, 0))
    new_image.save(image_path)



def crop_left(image_path, crop_width):
    original_image = Image.open(image_path)
    original_width, original_height = original_image.size

    new_width = original_width - crop_width
    cropped_image = original_image.crop((crop_width, 0, original_width, original_height))
    cropped_image.save(image_path)



image_path = "certificate.png"
padding_height = 300
padding_color = (255, 255, 255)  
crop_width = 200
add_bottom_padding(image_path, padding_height, padding_color)
crop_left(image_path, crop_width)
