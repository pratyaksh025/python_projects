import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("😎 Calculator")

        # store expression
        self.expression = ""

        # Display frame (label + backspace side by side)
        display_frame = tk.Frame(root)
        display_frame.grid(row=0, column=0, columnspan=4, pady=20, sticky="we")

        # Display label
        self.label = tk.Label(display_frame, text="0", font=("Arial", 40), anchor="e", bg="white", relief="sunken")
        self.label.pack(side="left", expand=True, fill="x", ipadx=10)

        # Backspace button
        backspace_btn = tk.Button(display_frame, text="⌫", width=5, font=("Arial", 20),
                                  command=self.backspace)
        backspace_btn.pack(side="right", padx=5)

        # Buttons layout
        buttons = [
            ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("+", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("/", 3, 3),
            (".", 4, 0), ("0", 4, 1), ("=", 4, 2), ("*", 4, 3)
        ]

        for (text, row, col) in buttons:
            action = (lambda val=text: self.on_button_click(val))
            btn = tk.Button(root, text=text, width=5, font=("Arial", 20), command=action)
            btn.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        """Handles button click for digits and operators"""
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.expression = result
                self.label.config(text=result)
            except Exception:
                self.label.config(text="Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.label.config(text=self.expression)

    def backspace(self):
        """Removes last character"""
        self.expression = self.expression[:-1]
        self.label.config(text=self.expression if self.expression else "0")


# Run app
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
