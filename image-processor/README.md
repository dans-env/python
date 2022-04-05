
README

   This python script will proccess images from a directory and save them into a new directory.

   Process:
      [1] Get the images from a directory and loop over them
      [2] Check that the file we are reading is a supported image file.
      [3] If the file is suported:
         try
            - We open the image
            - Convert the image to RGB
            - Check images size, if W or H is greater than 500, reduse the image size to 500 whilst keeping orginal image aspect ratio.
            - Save new processed image to new locations.
         else catch error
            - We print the file name to the console.
      [4] If file is not supported:
         - We print the file name to the console.

   Directories can be changed with vairable:
      variable original_path (The directory that you would like to read from)
      variable processed_path (The directory you would like to save the processed images too)

   Accepted file extentions for original images:
      accepted_exptentions ('.png', '.jpg', '.jpeg', '.tif', '.tiff', '.bmp', '.gif')

   Image size can be changed with:
      variable size (Can be changed to what ever is needed - only interger reqired)

   Hope this makes sense.

   Happy coding,
   Dan!