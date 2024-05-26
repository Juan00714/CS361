import tkinter as tk
from tkinter import ttk
import time

def save_inputs_to_file():
    from_currency = from_currency_entry.get()
    to_currency = to_currency_entry.get()
    amount = amount_entry.get()
    
    with open('currency_inputs.txt', 'w') as file:
        file.write(f"{from_currency}\n{to_currency}\n{amount}\n")

def check_result():
    try:
        with open('currency_result.txt', 'r') as file:
            result = file.read()
            result_label.config(text=result)
    except FileNotFoundError:
        pass
    root.after(1000, check_result)


root = tk.Tk()
root.title("Currency Converter")


from_currency_label = ttk.Label(root, text="From Currency:")
from_currency_label.grid(column=0, row=0, padx=10, pady=10)
from_currency_entry = ttk.Entry(root)
from_currency_entry.grid(column=1, row=0, padx=10, pady=10)

# 'to' currency textbox
to_currency_label = ttk.Label(root, text="To Currency:")
to_currency_label.grid(column=0, row=1, padx=10, pady=10)
to_currency_entry = ttk.Entry(root)
to_currency_entry.grid(column=1, row=1, padx=10, pady=10)

# amount textbox
amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(column=0, row=2, padx=10, pady=10)
amount_entry = ttk.Entry(root)
amount_entry.grid(column=1, row=2, padx=10, pady=10)

# save button
save_button = ttk.Button(root, text="Convert", command=save_inputs_to_file)
save_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# results label
result_label = ttk.Label(root, text="Converted Amount: ")
result_label.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Run 
root.after(1000, check_result)  # Check for result updates every second
root.mainloop()
