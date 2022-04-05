import os, os.path;

from PIL import Image;
from pathlib import Path;

size = 500;
original_path = './images-test/';
processed_path = './images-processed/';
accepted_exptentions = (
   '.png',
   '.jpg',
   '.jpeg',
   '.tif',
   '.tiff',
   '.bmp',
   '.gif'
);

def process_image():
   try:
      #get images name with out extention
      image_name = Path(original_path + image).stem;

      #open current image
      img = Image.open(original_path + image);

      #convert image to RGB
      processed_img = img.convert('RGB');

      #resize image if width or height is greater than 500
      if img.width > size or img.height > size:
         processed_img.thumbnail((size, size));

      #save new image
      processed_img.save(processed_path + image_name + '.jpg');

      #close image once modification are compete.
      img.close();
   except OSError as error:
      print(f'File currupt: {image}');

#main loop
for image in os.listdir(original_path):
   #check if image / file is a supported file
   if image.lower().endswith(accepted_exptentions):
      process_image();
   else:
      print(f'Cannot identify image file: {image} - file not supported.');
print(f'Image run complete!');
