import cv2
import pytesseract
import sys
pytesseract.pytesseract.tesseract_cmd=r'/usr/bin/tesseract'



img=cv2.imread('images/frog.jpeg')


text=pytesseract.image_to_string(img)
print(text)

sys.stdout=open("output.txt","w")
print (text)
sys.stdout.close()
