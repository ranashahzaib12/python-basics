import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk

# Set base directory on the F drive
BASE_DIR = "F:/FileManager"
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)  # Create the directory if it doesn't exist

# Initialize main window with a background color
root = tk.Tk()
root.title("Simple File Manager")
root.geometry("600x400")
root.configure(bg="#e6e6e6")  # Light gray background

# Function to browse and display contents of a directory
def browse_directory():
    folder = filedialog.askdirectory(initialdir=BASE_DIR)
    if folder and folder.startswith(BASE_DIR):
        path_var.set(folder)
        display_files(folder)
    else:
        messagebox.showerror("Error", "Please select a folder within the F: drive file manager directory.")

# Function to display files and directories in the chosen path
def display_files(path):
    file_list.delete(0, tk.END)  # Clear previous list
    try:
        for idx, item in enumerate(os.listdir(path)):
            color = "#f2f2f2" if idx % 2 == 0 else "#d9d9d9"  # Alternate row colors
            file_list.insert(tk.END, item)
            file_list.itemconfig(tk.END, {'bg': color})
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to create a new file or folder in BASE_DIR
def create_item():
    item_name = simpledialog.askstring("Create", "Enter file/folder name:")
    if item_name:
        path = os.path.join(path_var.get(), item_name)
        try:
            if '.' in item_name:
                open(path, 'w').close()  # Create a new file
            else:
                os.mkdir(path)  # Create a new folder
            display_files(path_var.get())
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Function to delete a selected file or folder
def delete_item():
    selected = file_list.get(tk.ACTIVE)
    if selected:
        path = os.path.join(path_var.get(), selected)
        try:
            if os.path.isfile(path):
                os.remove(path)  # Delete file
            else:
                shutil.rmtree(path)  # Delete folder
            display_files(path_var.get())
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Function to rename a selected file or folder
def rename_item():
    selected = file_list.get(tk.ACTIVE)
    if selected:
        new_name = simpledialog.askstring("Rename", "Enter new name:")
        if new_name:
            old_path = os.path.join(path_var.get(), selected)
            new_path = os.path.join(path_var.get(), new_name)
            try:
                os.rename(old_path, new_path)
                display_files(path_var.get())
            except Exception as e:
                messagebox.showerror("Error", str(e))

# Function to open a selected file
def open_item():
    selected = file_list.get(tk.ACTIVE)
    if selected:
        path = os.path.join(path_var.get(), selected)
        try:
            if os.path.isfile(path):
                os.startfile(path)  # Opens the file with default application
            else:
                display_files(path)  # If it's a folder, open it in file manager
                path_var.set(path)
        except Exception as e:
            messagebox.showerror("Error", str(e))

# GUI Layout with colors
path_var = tk.StringVar(value=BASE_DIR)

# Directory browsing section
path_entry = tk.Entry(root, textvariable=path_var, width=50, bg="#ffffff", fg="#333333")
path_entry.grid(row=0, column=0, padx=10, pady=10, sticky="we")
browse_btn = tk.Button(root, text="Browse", command=browse_directory, bg="#4CAF50", fg="white")
browse_btn.grid(row=0, column=1, padx=10, pady=10)

# File list display with alternating colors
file_list = tk.Listbox(root, selectmode=tk.SINGLE, width=60, height=20, bg="#f2f2f2", fg="#333333")
file_list.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Action buttons with color styling
btn_frame = tk.Frame(root, bg="#e6e6e6")
btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

open_btn = tk.Button(btn_frame, text="Open", command=open_item, bg="#4CAF50", fg="white")
open_btn.grid(row=0, column=0, padx=5)

create_btn = tk.Button(btn_frame, text="Create", command=create_item, bg="#2196F3", fg="white")
create_btn.grid(row=0, column=1, padx=5)

rename_btn = tk.Button(btn_frame, text="Rename", command=rename_item, bg="#FFC107", fg="black")
rename_btn.grid(row=0, column=2, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete", command=delete_item, bg="#f44336", fg="white")
delete_btn.grid(row=0, column=3, padx=5)

# Initialize by displaying files in BASE_DIR
display_files(BASE_DIR)

root.mainloop()
