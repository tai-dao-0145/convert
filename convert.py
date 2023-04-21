import nltk
import pandas as pd
import os
from nltk.tokenize import word_tokenize
from pdfreader import SimplePDFViewer
import re
import fitz
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams

import fitz # install using: pip install PyMuPDF
import spacy


def convert_pdf_to_text2(file_pdf):
    with open(file_pdf, 'rb') as pdf_file:
        laparams = LAParams()
        text = extract_text(pdf_file, laparams=laparams)
        # Sử dụng spaCy để phân tích cú pháp văn bản và phân tách các từ
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        text_with_spaces = ""
        for token in doc:
            if token.text[0].isalpha() and len(text_with_spaces) > 0 and text_with_spaces[-1] != " ":
                text_with_spaces += " "
            text_with_spaces += token.text
            text_with_spaces = text_with_spaces.replace('\n', '')
            text_with_spaces = text_with_spaces.replace('/ ', ' ')
            text_with_spaces = text_with_spaces.replace('.-', '.')
            text_with_spaces = re.sub(r"[©]", ' ', text_with_spaces)
        return text_with_spaces
print(convert_pdf_to_text2('CV/3.pdf'))
def convert_pdf_to_text(file_pdf):
    with open(file_pdf, 'rb') as pdf_file:
        laparams = LAParams(char_margin=2.0)
        text = extract_text(pdf_file, laparams=laparams)
        text = text.replace('\n', '')
        text = text.replace('…', '.')
        text = text.replace('. .', '.')
        text = text.replace('...', '.')
        text = text.replace('..', '.')
        text = re.sub(r"[•·●•;]", '.', text)
        text = re.sub(r"[©]", ' ', text)
    return text
print(convert_pdf_to_text('CV/3.pdf'))



# with open("dataTxt/4.txt", "r") as file:
#     text = file.read()
# print(text)

word_text=convert_pdf_to_text2('CV/fondend_dev1.pdf')

word_text = word_tokenize(word_text)
# print(nltk.pos_tag(word_text))

i = 1
data = []
for word, tag in nltk.pos_tag(word_text):
    data.append((i, word, tag, ''))
    if word == ".":
        i = i + 1
# print(data)


def convertToExcel10(data):
    if os.path.exists('dataExcel/1.xlsx'):
        print("...")
        df = pd.read_excel('dataExcel/1.xlsx', sheet_name='Sheet1')
        new_df = pd.DataFrame(data, columns=['Sentence #','Word', 'POS','Tag'])
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_excel('dataExcel/1.xlsx', sheet_name='Sheet1', index=True)
        print("Success")
    else:
        print("...")
        df = pd.DataFrame(data, columns=['Sentence #','Word', 'POS','Tag'])
        df.to_excel('dataExcel/1.xlsx')
        print("Success")
# convertToExcel10(data)


def ExceltoTxt(file):
    df = pd.read_excel(file)

    # Lưu dữ liệu vào file text
    with open('dataTxt/file5.txt', 'w') as f:
        # Viết tiêu đề
        f.write("\tSentence #\tWord\tPOS\tTag\n")
        # Viết dữ liệu
        for index, row in df.iterrows():
            sentence = str(row['Sentence #'])
            word = str(row['Word'])
            pos = str(row['POS'])
            tag = " "  # Tag mặc định là khoảng trắng
            f.write(str(index)+"\t"+sentence + "\t" + word + "\t" + pos + "\t" + tag + "\n")
# ExceltoTxt("dataExcel/final22.xlsx")