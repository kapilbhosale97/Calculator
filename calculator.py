import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("300x400")
        self.window.resizable(False, False)
        
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Display
        display = tk.Entry(self.window, textvariable=self.result_var, font=("Arial", 16), 
                          justify="right", state="readonly", bg="white")
        display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="ew")
        
        # Buttons
        buttons = [
            ('AC', 1, 0), ('⌫', 1, 1), ('%', 1, 2), ('÷', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 2), ('=', 5, 3)
        ]
        
        for (text, row, col) in buttons:
            if text == '0':
                btn = tk.Button(self.window, text=text, font=("Arial", 14),
                               command=lambda t=text: self.button_click(t))
                btn.grid(row=row, column=col, columnspan=2, padx=2, pady=2, sticky="ew")
            else:
                btn = tk.Button(self.window, text=text, font=("Arial", 14),
                               command=lambda t=text: self.button_click(t))
                btn.grid(row=row, column=col, padx=2, pady=2, sticky="ew")
        
        # Configure grid weights
        for i in range(4):
            self.window.grid_columnconfigure(i, weight=1)
    
    def button_click(self, char):
        current = self.result_var.get()
        
        if char == 'C':
            self.result_var.set("0")
        elif char == '=':
            try:
                expression = current.replace('×', '*').replace('÷', '/')
                result = str(eval(expression))
                self.result_var.set(result)
            except:
                messagebox.showerror("Error", "Invalid expression")
                self.result_var.set("0")
        elif char == '±':
            if current != "0":
                if current.startswith('-'):
                    self.result_var.set(current[1:])
                else:
                    self.result_var.set('-' + current)
        elif char == '⌫':
            if len(current) > 1:
                self.result_var.set(current[:-1])
            else:
                self.result_var.set("0")
        elif char == '%':
            try:
                result = str(float(current) / 100)
                self.result_var.set(result)
            except:
                messagebox.showerror("Error", "Invalid operation")
        else:
            if current == "0" and char.isdigit():
                self.result_var.set(char)
            else:
                self.result_var.set(current + char)
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()