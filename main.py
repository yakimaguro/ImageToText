import os
from PIL import Image, UnidentifiedImageError
import pyocr
from tkinter import filedialog
import tkinter as tk

pyocr.tesseract.TESSERACT_CMD = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

root = tk.Tk()
root.title("tk")
root.geometry("600x200+30+30")

typ = [('すべてのファイル', '*')]
dir = 'C:\\'
file = filedialog.askopenfilename(filetypes=typ, initialdir=dir)

# OCRエンジンを取得
engines = pyocr.get_available_tools()
engine = engines[0]

# 画像の文字を読み込む
txt = engine.image_to_string(Image.open(file), lang="jpn")
print(txt)