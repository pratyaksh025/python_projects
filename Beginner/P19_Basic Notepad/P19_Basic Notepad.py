import os

def save_text(filename, text):
    with open(filename, "w") as f:
        f.write(text)
    print("Text saved successfully!")

def load_text(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
        print("\nLoaded text:\n")
        print(content)
    except FileNotFoundError:
        print("No saved file found!")



filename = "notes.txt"
file_destination = os.path.join(os.getcwd(),filename)
while True:
    print("\n--- Basic Notepad ---")
    print("1. Write new text")
    print("2. Save text")
    print("3. Load text")
    print("4. Exit")
    
    choice = input("Choose option: ")

    if choice == "1":
        text = input("Enter your text: ")
    elif choice == "2":
        save_text(file_destination, text)
    elif choice == "3":
        load_text(file_destination)
    elif choice == "4":
        print("App Closed")
        break
    else:
        print("Invalid choice! Try again.")
