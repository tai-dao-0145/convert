import fitz
import re


def convertPDFToText(filename):
    link = r"CV/" + filename + ".pdf"
    with fitz.open(link) as pdf_file:
        for page in pdf_file:
            page_content = page.get_text()
            page_content = re.sub(r'\s{2,}', ' ', page_content)  # Loại bỏ khoảng trắng thừa
            # page_content = re.sub(r'[^\w\s]', ' ', page_content)  # Loại bỏ các kí tự đặc biệt
            page_content = re.sub(r'[():""\n]', '', page_content)
            page_content = re.sub(r'\n\s*\n', '\n', page_content)
            page_content = re.sub(r"[•·●•;]", '.', page_content)
            page_content = re.sub(r'[+:/]', '', page_content)
            page_content = page_content.replace('Job description', 'Job description .')
            page_content = page_content.replace('.-', '.')
            page_content = page_content.replace('…', '.')
            page_content = page_content.replace('. .', '.')
            page_content = page_content.replace('...', '.')
            page_content = page_content.replace('..', '.')
            with open('cvTxt/' + filename + ".txt", 'a', encoding="utf-8") as file:
                file.write(page_content)
            print(page_content)

convertPDFToText("1")


            # Tách nội dung thành các dòng và kiểm tra kí tự xuống dòng
            # lines = page_content.splitlines()
            # for i, line in enumerate(lines):
            #     # if line == "Salary " or line == "Agree ":
            #     # else:
            #     if line:
            # page_content = page_content.replace('..', '.')
