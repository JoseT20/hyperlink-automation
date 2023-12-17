""" import tkinter as tk
import tkinter.filedialog as fd

root = tk.Tk()
files = fd.askopenfilenames(parent=root, title='Choose a file')

for file in files:
    print() """

import tkinter as tk
import os
import main
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

def select_files():
    filetypes = (("text files", "*.txt"), ("All files", "*.*"))

    global files 
    files = fd.askopenfilenames(title="Open files", initialdir="/", filetypes=filetypes)

    if files:
        read_files(files)


def hyperlink_files():
    for file in files:
        main.move_file(os.path.basename(file), file_path=file)
        new_file_path = f"{main.target_directory}/{file}"
        main.create_hyperlink(new_file_path, os.path.basename(file))

    remove_all()


def read_files(files):
    if not table_empty():
        remove_all()

    for index, file in enumerate(files):
        file_list.insert("", tk.END, iid=index, values=[os.path.basename(file), main.get_target_directory(os.path.basename(file))])

def table_empty():
    if file_list.size == [0, 0]:
        return True
    
def remove_all():
    file_list.delete(*file_list.get_children())

def remove_selected():
    try:
        selected_item = file_list.selection()
    except Exception:
        return
    file_list.delete(*selected_item)
    

# create the root window
root = tk.Tk()
root.title("Hyperlink-Automation")
root.geometry("735x325")

# open button
open_button = ttk.Button(root, text="Choose Files", command=select_files).grid(
    row=0, column=0, sticky="w", padx=15, pady=10
)

# files table
file_list = ttk.Treeview(
    root, height=10, show="headings", columns=("File Name", "Target Folder")
)
file_list.grid(row=1, column=0, columnspan=3, padx=15, sticky="w")
ttk.Style().map("Treeview", background=[("selected", "grey")])
file_list.heading("File Name", text="File Name", anchor="center")
file_list.column("File Name", width=280)
file_list.heading("Target Folder", text="Target Folder", anchor="center")
file_list.column("Target Folder", width=420)

# button frame
button_frame = ttk.Frame(root)
button_frame.grid(row=2, column=0, columnspan=2, padx=15, pady=10, sticky="w")

# remove button
remove_selected_button = ttk.Button(button_frame, text="Remove", command=remove_selected)
remove_selected_button.grid(row=0, column=0)

# remove all button
remove_all_button = ttk.Button(button_frame, text="Remove All", command=remove_all)
remove_all_button.grid(row=0, column=1, padx=10)

# create hyperlink button
create_hyperlink_button = ttk.Button(
    root, text="Create Hyperlink", command=hyperlink_files
)
create_hyperlink_button.grid(row=2, column=2, sticky="e", padx=15, pady=10)

root.mainloop()
