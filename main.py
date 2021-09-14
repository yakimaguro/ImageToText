import os
from PIL import Image, UnidentifiedImageError
import pyocr
from tkinter import filedialog
import tkinter as tk

pyocr.tesseract.TESSERACT_CMD = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

root = tk.Tk()
root.title("Python OCR Test")
root.geometry("700x500")

engines = pyocr.get_available_tools()
engine = engines[0]


def load():
    typ = [('すべてのファイル', '*')]
    dir = 'C:\\'
    file = filedialog.askopenfilename(filetypes=typ, initialdir=dir)
    global txt
    txt = engine.image_to_string(Image.open(file), lang="jpn")
    output()


def output():
    textbox.insert(tk.END, txt)


def copy_text():
    txt = textbox.get()
    root.clipboard_append(txt)


loadbtn = tk.Button(root, text="画像読み込み", font=("Meiryo UI", 18), command=load)
loadbtn.pack(expand=1)

textbox = tk.Entry(font=("Meiryo UI", 18), width=30)
textbox.pack(expand=10)

copybtn = tk.Button(root, text="テキストをクリップボードにコピー", font=("Meiryo UI", 18), command=copy_text)
copybtn.pack(expand=1)

root.mainloop()



