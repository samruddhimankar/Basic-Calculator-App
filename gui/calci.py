import tkinter as tk
from tkinter import messagebox
def perform_operation(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")
def clear_inputs():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Result: ")
# Create the main application window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x300")
# Input fields and labels
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()
label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()
# Frame for operation buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
# Buttons for operations (2x2 grid)
button_add = tk.Button(button_frame, text="Add", command=lambda: perform_operation("Addition"))
button_add.grid(row=0, column=0, padx=5, pady=5)
button_subtract = tk.Button(button_frame, text="Subtract", command=lambda: perform_operation("Subtraction"))
button_subtract.grid(row=0, column=1, padx=5, pady=5)
button_multiply = tk.Button(button_frame, text="Multiply", command=lambda: perform_operation("Multiplication"))
button_multiply.grid(row=1, column=0, padx=5, pady=5)
button_divide = tk.Button(button_frame, text="Divide", command=lambda: perform_operation("Division"))
button_divide.grid(row=1, column=1, padx=5, pady=5)
# Button to clear input
button_clear = tk.Button(root, text="Clear", command=clear_inputs)
button_clear.pack(pady=5)
# Label to display result
label_result = tk.Label(root, text="Result: ")
label_result.pack(pady=10)
# Run the application
root.mainloop()
