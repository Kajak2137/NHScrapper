import img2pdf
from os import listdir
from os import path


def convert_pdf(title):
    sauce_dir = title + "/"
    filename = sauce_dir + title + ".pdf"
    img_table = []
    try:
        for file in listdir(sauce_dir):
            if file.endswith(".jpg"):
                img_table.append(path.join(sauce_dir, file))
            else:
                pass
        pdf_bytes = img2pdf.convert(img_table)
        file = open(filename, "wb")
        file.write(pdf_bytes)
        return 1
    except Exception as e:
        return e


def convert_mobi(title):
    pass


def convert_epub(title):
    pass
