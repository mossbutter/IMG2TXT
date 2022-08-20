# IMG2TXT
Python script using opencv+tesseract that reads images and spits the output into a .txt file.

## Prerequisites:
Python3
tesseract OCR https://github.com/tesseract-ocr/tesseract
openCV https://opencv.org/


## Set-up:
Change the tesseract directory, yours may be the same 
```
pytesseract.pytesseract.tesseract_cmd=r'/usr/bin/tesseract'
```

Point the code to your image directory
```
img=cv2.imread('img.jpeg')
```
```
img=cv2.imread('images/img.jpeg')
```

## Use:
After updating your directories, make sure the script.py and images are in the same working directory.
Run the script and the text will display in your terminal, and in your **output.txt** file.

### Tips:
- you will have to change the image directory everytime you want to read a new image
- this is still in active development
- the text will overwrite itself in **output.txt**
- works better with larger resolution images

it's a small, simple program - I've included 2 sample images in **/images**. You can see how it will do it's best to read text that's laid over an image, but it isn't perfect. this is better suited for large walls of text or data you want to rip ASAP.

this project will continuously update as I learn more! enjoy
