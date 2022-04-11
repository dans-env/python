import os, os.path;

from PIL import Image;
from pathlib import Path;

size = 500;
image_path = './images/';
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
   img = Image.open(image_path + image);

   if img.width > size or img.height > size:
      img.thumbnail((size, size));

   img.save(image_name);
   img.close();

#main loop
for image in os.listdir(image_path):
   #check if image / file is a supported file
   if image.lower().endswith(accepted_exptentions):
      image_name = Path(image_path + image);
      resize_image(image_name);
   else:
      print(f'Cannot identify image file: {image} - file not supported.');

print("Image run complete!");
