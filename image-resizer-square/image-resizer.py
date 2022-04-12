import os, os.path;

from PIL import Image;
from pathlib import Path;

size = 400;
background = "./background/default-background.jpg";
image_path = './images/';
save_location = "./resized_images/";
accepted_exptentions = (
   '.png',
   '.jpg',
   '.jpeg',
   '.tif',
   '.tiff',
   '.bmp',
   '.gif'
);

def resize_image(image_name):
   background_img = Image.open(background);
   img = Image.open(image_path + image);

   img = img.convert('RGB');

   if img.width > size or img.height > size:
      img.thumbnail((size, size));

   position = ((int(background_img.width / 2) - int(img.width / 2)), (int(background_img.width / 2) - int(img.height / 2)));
   background_img_copy = background_img.copy();
   background_img_copy.paste(img, position)

   background_img_copy.save(save_location + image_name + '.jpg');
   img.close();

#main loop
for image in os.listdir(image_path):
   #check if image / file is a supported file
   if image.lower().endswith(accepted_exptentions):
      image_name = Path(image_path + image).stem;
      resize_image(image_name);
   else:
      print(f'Cannot identify image file: {image} - file not supported.');

print("Image run complete!");