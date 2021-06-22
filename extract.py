import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import simpledialog


# Entries is an array of arrays. The inner array contains three form boxes. [0] = Start page, [1] = end page, [2] = name of aria.
def extract(entries, pdf_filename):
    page_info = get_info(entries)
    dir_name = create_dir()
    extract_pages(page_info, pdf_filename, dir_name)

    print(page_info)


def get_info(entries):
    page_info = []
    for i, entry in enumerate(entries):
        try:
            start = int(entry[0].get())
            end = int(entry[1].get())
            name = str(i + 1) + ". " + str(entry[2].get())
            if start > 0 and start < 10000 and end > 0 and end < 10000:
                page_info.append([start, end, name])
        except ValueError:
            break
    return page_info


def create_dir():
    dir_name = "output/" + \
        simpledialog.askstring("Folder", "Enter output folder name: ")
    if not os.path.exists("output"):
        os.mkdir("output")
        print("Directory ", "output",  " Created ")
    else:
        print("Directory ", "output",  " already exists")
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print("Directory ", dir_name,  " Created ")
    else:
        print("Directory ", dir_name,  " already exists")
    return dir_name


def extract_pages(page_info, pdf_filename, dir_name):
    for info in page_info:
        extract_one(info, pdf_filename, dir_name)


def extract_one(info, pdf_filename, dir_name):
    full_dir_name = os.getcwd() + "/" + dir_name
    with open(pdf_filename, 'rb') as infile:
        reader = PdfFileReader(infile)
        if reader.isEncrypted:
            reader.decrypt('')
        writer = PdfFileWriter()
        for i in range(info[0] - 1, info[1]):
            writer.addPage(reader.getPage(i))
        with open(full_dir_name + "/" + info[2] + ".pdf", 'wb') as outfile:
            writer.write(outfile)
