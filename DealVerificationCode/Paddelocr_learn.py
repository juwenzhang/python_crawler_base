import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"E:\pycharm\pip\tesseract\Tesseract-OCR\tesseract.exe"

image = Image.open("./demo.jpg")

text = pytesseract.image_to_string(image)

print(text.upper())