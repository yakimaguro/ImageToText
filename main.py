import os
from PIL import Image, UnidentifiedImageError
import pyocr
from tkinter import filedialog
import tkinter as tk

pyocr.tesseract.TESSERACT_CMD = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

root = tk.Tk()
root.title("tk")
root.geometry("700x500")

def test():
    txtbox1.insert(tk.END, "1234")

def clear_text():
    txtbox1.delete(0, tk.END)

def copy_text():
    txt = txtbox1.get()
    print(txt)
    root.clipboard_append(txt)  # ここがクリップボードへのコピーをする処理

button1 = tk.Button(root, text="サンプル文字を出力", font=("Meiryo UI",18), command=test)
button1.pack(expand=1)

txtbox1 = tk.Entry(font=("Meiryo UI",18), width=30)
txtbox1.pack(expand=1)

button2 = tk.Button(root, text="テキストボックス内をクリア", font=("Meiryo UI",18), command=clear_text)
button2.pack(expand=1)

button3 = tk.Button(root, text="テキストボックス内をコピー", font=("Meiryo UI",18), command=copy_text)
button3.pack(expand=1)

root.mainloop()

# typ = [('すべてのファイル', '*')]
# dir = 'C:\\'
# file = filedialog.askopenfilename(filetypes=typ, initialdir=dir)
#
# # OCRエンジンを取得
# engines = pyocr.get_available_tools()
# engine = engines[0]
#
# # 画像の文字を読み込む
# txt = engine.image_to_string(Image.open(file), lang="jpn")
# print(txt)