import pytesseract

from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
phrase = pytesseract.image_to_string(Image.open('tesseract.PNG'))
print(phrase)
