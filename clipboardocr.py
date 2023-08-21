from PIL import Image, ImageGrab
from time import sleep
from pytesseract import pytesseract
from io import BytesIO
from clipboard import copy


pytesseract.tesseract_cmd = 'D:/Program Files/Tesseract-OCR/tesseract.exe'
old_bytes = '' 

while True:
    sleep(0.2)
    try:
        bio = BytesIO() 
        if old_bytes == bio:
            continue
        cbgrab = ImageGrab.grabclipboard()
        if cbgrab:
            cbgrab.convert('RGB').save(bio, 'JPEG') # adding image data to bytes object
            bio.seek(0) # Very important, seeks to start
            copy(pytesseract.image_to_string(Image.open(bio)))
            old_bytes = bio
    except Exception as e:
        print(e)
