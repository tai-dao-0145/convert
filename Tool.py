import nltk
import pandas as pd
import os
from nltk.tokenize import word_tokenize
from pdfreader import SimplePDFViewer
import re
import fitz




# def convertPDFToText(filename):
#     link = r"CV/" + filename + ".pdf"
#     with fitz.open(link) as pdf_file:
#         for page in pdf_file:
#             page_content = page.get_text()
#             page_content = re.sub(r'[():""\n]', '', page_content)
#             page_content = re.sub(r'\n\s*\n', '\n', page_content)
#             page_content = re.sub(r"[•·●•;]", '.', page_content)
#             # page_content = page_content.replace('Job description', 'Job description .')
#             page_content = page_content.replace('…', '.')
#             page_content = page_content.replace('. .', '.')
#             page_content = page_content.replace('...', '.')
#             page_content = page_content.replace('..', '.')
#             with open('dataTxt/' + filename + ".txt", 'a', encoding="utf-8") as file:
#                 file.write(page_content)
#             print(page_content)

# for i in range(1, 42, 1):
#     convertPDFToText(str(i))

def convertToExcel10(textC):
    text = word_tokenize(textC)
    nltk.pos_tag(text)
    if os.path.exists('dataExcel/1.xlsx'):
        print("...")
        df = pd.read_excel('dataExcel/1.xlsx', sheet_name='Sheet1')
        new_df = pd.DataFrame(nltk.pos_tag(text), columns=['Word', 'POS'])
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_excel('dataExcel/1.xlsx', sheet_name='Sheet1', index=True)
        print("Success")
    else:
        print("...")
        df = pd.DataFrame(nltk.pos_tag(text), columns=['Word', 'POS'])
        df.to_excel('dataExcel/1.xlsx', index=True)
        print("Success")


for i in range(1, 23, 1):
    file = r"fileTxt/" + str(i) + ".txt"
    with open(file, 'r', encoding="utf8") as f:
        content = f.read()
    convertToExcel10(content)


# for i in range(1, 42, 1):
#     file = r"dataTxt/" + str(i) + ".txt"
# with open("cvTxt/1.txt", 'r', encoding="utf8") as f:
#     content = f.read()
#
# convertToExcel10(content)
