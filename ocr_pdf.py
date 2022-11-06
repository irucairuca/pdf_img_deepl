# -*- coding: utf-8 -*-
from PIL import Image
import sys
import pyocr
import pyocr.builders
import pdf2image
#pdfファイルを探す時にカレントパスを取得するために必要
import os
# GUI
from tkinter import filedialog
import deepl


tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'


cwd = os.getcwd()#カレントディレクトリを取得



typ = [('PDFファイル','*.pdf')]#pdfアップロード
dir = cwd
fle = filedialog.askopenfilename(filetypes = typ, initialdir = dir)


txt1=""
# pdfから画像オブジェクトに
images = pdf2image.convert_from_path(fle, dpi=200, fmt='jpg')
lang = 'eng'
#lang = 'jpn'
# 画像オブジェクトからテキストに
for image in images:
    txt = tool.image_to_string(
        image,
        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )
    #print(txt)
    txt1 += txt

#https://dev.classmethod.jp/articles/export-text-data-from-image-using-python/






#OCR後の文章がテキストファイルとして出力される

filename=os.path.basename(fle).split('.', 1)[0]#ファイル名
f = open(filename+'_ocr.txt', 'w')
f.write(txt1)
f.close()


print("OCRが無事完了しました")



API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # 自身の API キーを指定

text = str(txt1)
source_lang = 'EN'
target_lang = 'JA'

# イニシャライズ
translator = deepl.Translator(API_KEY)

# 翻訳を実行
result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)

# print すると翻訳後の文章が出力される
print(result)

result = str(result)

#OCR後の文章がテキストファイルとして出力される

filename=os.path.basename(fle).split('.', 1)[0]#ファイル名
f = open(filename+'_ocr_ja.txt', 'w')
f.write(result)
f.close()


print("英語から日本語への翻訳が無事完了しました")
