# GUI
import os
from tkinter import filedialog, messagebox
import customtkinter as ctk
import source as src
from datetime import datetime


def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_entry.insert(0, folder_selected)


def start_process():
    if not os.path.exists(text_type.get()):
        return messagebox.showerror("Folder Err",
                                    "There is no any folder found as the input location!\nPlease check the Directory")
    time_start = datetime.now()
    obj = src.Extension()
    obj.__file_path__ = text_type.get()
    obj.separate()
    total_files_label.configure(text=f"Total Files: {obj.moves}")
    time_end = datetime.now()
    print(time_end - time_start)
    messagebox.showinfo("Process Completed", f"The data file have been moved there folder Successfully!\n"
                                             f"Time Take: {time_end-time_start} Sec")


# Initialize the main window
app = ctk.CTk()
app.title("Organize Your Files and Time!")
app.geometry("450x290")
app.resizable(False, False)
app.iconbitmap("logo.ico")
option_type = ctk.StringVar()
text_type = ctk.StringVar()
 
# Configure grid layout
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)

blank = ctk.CTkLabel(app, text="")
blank.grid(row=0)

# Folder selection section
folder_label = ctk.CTkLabel(app, text="Select Folder:", font=("Century Gothic", 20, "bold"))
folder_label.grid(row=1, columnspan=2, pady=5, padx=35, sticky='w')

folder_entry = ctk.CTkEntry(app, width=250, font=("Century Gothic", 14), textvariable=text_type)
folder_entry.grid(row=2, column=0, pady=10, padx=10)

browse_button = ctk.CTkButton(app, text="Browse", command=browse_folder, font=("Century Gothic", 18), width=15)
browse_button.grid(row=2, column=1, pady=10)

# Type selection section
type_label = ctk.CTkLabel(app, text="Select Type:", font=("Century Gothic", 20, "bold"))
type_label.grid(row=3, columnspan=2, pady=5, padx=35, sticky='w')

type_combobox = ctk.CTkComboBox(app, values=["File Type Grouping", "Extension-Based Sorting"], width=250,
                                variable=option_type, font=("Century Gothic", 14))
type_combobox.grid(row=4, column=0, pady=10, padx=10)
type_combobox.set("Extension-Based Sorting")

# Start button
start_button = ctk.CTkButton(app, text="Start", command=start_process, font=("Century Gothic", 18), width=75)
start_button.grid(row=4, column=1, pady=20)

# Total files label
total_files_label = ctk.CTkLabel(app, text="Total Files: 0", font=("Century Gothic", 16, "italic"))
total_files_label.grid(row=5, columnspan=2, pady=10)

# Run the application
app.mainloop()
