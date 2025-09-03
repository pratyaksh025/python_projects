# Basic Notepad 📝  

This is a simple **Basic Notepad application** built with Python. It allows users to write, save, and load text files directly from the console.  

---

## How It Works  
1. When you run the program, a menu appears with options:  
   - **1. Write new text** → Enter any text you want.  
   - **2. Save text** → Saves the text into a file (`notes.txt`).  
   - **3. Load text** → Loads and displays saved text from the file.  
   - **4. Exit** → Closes the application.  

2. The file is stored at:  
    
    ```css
    file_destination = os.path.join(os.getcwd(),filename)
    ```


3. If you try to load text before saving, it will show **"No saved file found!"**  


## Example Usage  

```yaml
--- Basic Notepad ---

1. Write new text
2. Save text
3. Load text
4. Exit
Choose option: 1

Enter your text: Hello, this is my first note!

--- Basic Notepad ---

1. Write new text
2. Save text
3. Load text
4. Exit
Choose option: 2
Text saved successfully!

--- Basic Notepad ---

1. Write new text
2. Save text
3. Load text
4. Exit
Choose option: 3

Loaded text:

Hello, this is my first note!
```

## Features  
- Write and save notes to a file.  
- Load previously saved notes.  
- Handles missing file errors gracefully.  
- Simple text-based menu.  

---

## How to Run  
1. Make sure Python is installed.  
2. Save the script as `P19_Basic_Notepad.py`.  
3. Run it using:  
   ```bash
   python P19_Basic_Notepad.py
   ```

## Future Improvements 🚀

- Support for multiple notes/files.

- Option to append instead of overwrite.

- GUI version using Tkinter or PyQt.

## Author
Made with ❤️ by Pratyaksh Yadav