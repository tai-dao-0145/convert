
import nltk
import pandas as pd
import os
from nltk.tokenize import word_tokenize
from pdfreader import SimplePDFViewer
import re
import fitz



with open('fileTxt/5.txt', 'r') as file:
    page_content = file.read()

print(page_content)
print("\n")
page_content = re.sub(r'[()""\n]', '', page_content)
# page_content = re.sub(r'\n\s*\n', '\n', page_content)
# page_content = re.sub(r"[•·●•;]", '.', page_content)
# page_content = re.sub(r'[+:/€¢()]', '', page_content)
page_content = page_content.replace('.-', '.')
page_content = page_content.replace("\n", '.')
page_content = page_content.replace('…', '.')
page_content = page_content.replace('. .', '.')
page_content = page_content.replace('...', '.')
page_content = page_content.replace('..', '.')
print(page_content)

def convertToExcel10(textC):
    text = word_tokenize(textC)
    nltk.pos_tag(text)
    if os.path.exists('dataExcel/3.xlsx'):
        print("...")
        df = pd.read_excel('dataExcel/3.xlsx', sheet_name='Sheet1')
        new_df = pd.DataFrame(nltk.pos_tag(text), columns=['Word', 'POS'])
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_excel('dataExcel/3.xlsx', sheet_name='Sheet1', index=True)
        print("Success")
    else:
        print("...")
        df = pd.DataFrame(nltk.pos_tag(text), columns=['Word', 'POS'])
        df.to_excel('dataExcel/3.xlsx', index=True)
        print("Success")
# convertToExcel10(page_content)



# # for i in range(1, 42, 1):
# #     file = r"dataTxt/" + str(i) + ".txt"
# with open("fileTxt/tt.txt", 'r', encoding="utf8") as f:
#     content = f.read()
#
# convertToExcel10(content)

