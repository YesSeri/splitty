import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Splitty")
root.geometry("500x500+0+0")
frame = tk.Frame(root)
frame.grid(row=0, column=0)
side_frame = tk.Frame(root)
side_frame.grid(row=0, column=1)


# Global Variables
row = 1
entries = []
pdf_filename = ""
def add_row():
    global row
    start_e = tk.Entry(frame, width=5)
    start_e.grid(row=row, column=0, ipady=3)
    end_e = tk.Entry(frame, width=5)
    end_e.grid(row=row, column=1, ipady=3)
    entries.append([start_e, end_e])
    row += 1

def save():
    output = entries[0][0].get() 
    page_numbers = []
    for entry in entries:
        try:
            start = int(entry[0].get())
            end = int(entry[1].get())
            if start > 0 and start < 10000 and end > 0 and end < 10000:
                page_numbers.append([start, end])
        except ValueError:
            break

    print(page_numbers)

    # Set active PDF
def select_pdf():
    global pdf_filename
    pdf_filename = filedialog.askopenfilename(initialdir=os.getcwd(), title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))

# 10 inital rows. Add more with add button
for i in range(0,10):
    add_row()

# Creating gui

start_label = tk.Label(frame, text="Start")
end_label = tk.Label(frame, text="End")
add_button = tk.Button(frame, text="Add", command=add_row, width=5)
save_button = tk.Button(frame, text="Save", command=save, width=5)
pdf_button = tk.Button(frame, text="PDF", command=select_pdf, width=5)

# Adding gui to grid

save_button.grid(row=0, column=2)
pdf_button.grid(row=1, column=2)
add_button.grid(row=2, column=2)
start_label.grid(row=0, column=1)
end_label.grid(row=0, column=0)

root.mainloop()
