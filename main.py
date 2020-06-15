from extract import *
import tkinter as tk
from tkinter import filedialog

# Global Variables
row = 2
entries = []
pdf_filename = ""

root = tk.Tk()
root.title("Splitty")
root.geometry("1010x1010+0+0")
frame0 = tk.Frame(root)
frame1 = tk.Frame(root)
frame0.grid(row=0, column=0)
frame1.grid(row=2, column=0)
#root.grid_rowconfigure(1, weight=1)
def add_row():
    global row

    start_entry = tk.Entry(frame0, width=5)
    end_entry = tk.Entry(frame0, width=5)
    name_entry = tk.Entry(frame0, width=100)

    start_entry.grid(row=row, column=0, ipady=3)
    end_entry.grid(row=row, column=1, ipady=3)
    name_entry.grid(row=row, column=2, ipady=3)

    entries.append([start_entry, end_entry, name_entry])
    row += 1
def select_pdf():
    global pdf_filename
    pdf_filename = filedialog.askopenfilename(initialdir=os.getcwd(), title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
    pdf_label.config(text=os.path.basename(os.path.normpath(pdf_filename)))

# 10 inital rows. Add more with add button
for i in range(0,2):
    add_row()

# Creating gui

start_label = tk.Label(frame0, text="Start")
end_label = tk.Label(frame0, text="End")
name_label = tk.Label(frame0, text="Name")

add_button = tk.Button(frame1, text="Add", command=add_row)
pdf_button = tk.Button(frame1, text="PDF", command=select_pdf)
extract_button = tk.Button(frame1, text="Extract", command=lambda: extract(entries, pdf_filename))

pdf_label = tk.Label(frame1, text="PDF")

# Adding gui to grid

start_label.grid(row=1, column=0)
end_label.grid(row=1, column=1)
name_label.grid(row=1, column=2)

add_button.grid(row=0, column=0)
pdf_button.grid(row=0, column=1)
extract_button.grid(row=0, column=2)

pdf_label.grid(row=0, column=3)

root.mainloop()
