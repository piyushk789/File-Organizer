# File Organizer

**File Organizer** is a Python-based tool designed to help users easily manage and organize their files. The program moves files into folders named after their file extensions. For example, `.png` files are moved into a "png" folder, `.jpg` into a "jpg" folder, `.pdf` into a "pdf" folder, and so on.

### Features:
- Automatically moves files into folders based on their extensions (e.g., `.png` into a "PNG" folder, `.exe` into an "EXE" folder, etc.)
- Simple and intuitive graphical user interface (GUI)
- Two Python files for easy separation of concerns: GUI and backend
- Cross-platform compatibility

### How it works:
The program scans a specified directory, identifies file extensions, and moves the files into corresponding folders based on their extensions. The program categorizes various types of files such as `.png`, `.jpg`, `.pdf`, `.exe`, and more, making file organization simple and efficient.

### Project Structure:
1. **gui.py**: This file handles the graphical user interface, designed using `customtkinter` and `tkinter` libraries.
2. **Source.py**: This file contains the backend code, handling the file operations such as scanning directories and moving files using the `os` module.

### Requirements:
- Python 3.x
- Required Python packages: 
  - `os`
  - `customtkinter`
  - `tkinter`
  
### How to Use:
1. Clone or download the repository.
2. Run the `gui.py` file to launch the graphical user interface.
3. Specify the directory you want to organize, and the program will automatically categorize and move files into folders based on their extensions.

   
