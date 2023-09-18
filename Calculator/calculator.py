import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Calculator by Hemanth")
        root.configure(bg="black")  # Set the background color to black
        
        self.result_var = tk.StringVar()
        self.result_var.set("")
        
        # Entry widget for displaying the input and result
        self.entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 20), bd=0, justify="right", bg="black", fg="white")  # Set text color to white
        self.entry.grid(row=0, column=0, columnspan=4)
        
        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'AC', '0', '=', '+'
        ]
        
        row, col = 1, 0
        for button_text in buttons:
            tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 16),
                      command=lambda t=button_text: self.on_button_click(t), bg="black", fg="white").grid(row=row, column=col)  # Set button colors
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.current_input = ""

    def on_button_click(self, button_text):
        if button_text == "=":
            try:
                result = str(eval(self.current_input))
                self.result_var.set(result)
                self.current_input = result
            except Exception as e:
                self.result_var.set("Error")
                self.current_input = ""
        elif button_text == "AC":
            self.result_var.set("")
            self.current_input = ""
        else:
            self.current_input += button_text
            self.result_var.set(self.current_input)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
