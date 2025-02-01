import tkinter as tk

def press_number(num, entry_widget):
    """Handles button clicks for numbers, inserting into the active input box."""
    current_text = entry_widget.get()
    entry_widget.delete(0, tk.END)
    entry_widget.insert(tk.END, current_text + str(num))

def update_result():
    """Performs calculation based on selected operator and inputs, and updates result."""
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operation_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result_label.config(text="Error: Cannot divide by zero!", fg="red", font=("Arial", 14, "bold"))
                return
        else:
            result_label.config(text="Error: Select an operation!", fg="red", font=("Arial", 14, "bold"))
            return

        # Display result in a bold and attractive way
        result_label.config(text=f"= {result}", fg="white", font=("Arial", 21, "bold"))

    except ValueError:
        result_label.config(text="Error: Enter valid numbers!", fg="red", font=("Arial", 14, "bold"))

def clear(entry_widget):
    """Clears the selected entry field."""
    entry_widget.delete(0, tk.END)
    result_label.config(text="")  # Clear result label as well

# Create main window
root = tk.Tk()
root.title("Enhanced Clickable Calculator")
root.geometry("350x500")
root.configure(bg="#2C3E50")

# Labels and Entry Fields
tk.Label(root, text="Enter first number:", font=("Arial", 12), bg="#2C3E50", fg="white").pack(pady=5)
entry1 = tk.Entry(root, font=("Arial", 12), width=15)
entry1.pack(pady=5)

# Number Buttons for First Entry
num_frame1 = tk.Frame(root, bg="#2C3E50")
num_frame1.pack()
for i in range(10):
    tk.Button(num_frame1, text=str(i), font=("Arial", 10), width=3, height=1, bg="#34495E", fg="white",
              command=lambda n=i: press_number(n, entry1)).grid(row=i // 5, column=i % 5, padx=3, pady=3)

# Clear Button for First Entry
tk.Button(root, text="Clear", font=("Arial", 8), bg="#E74C3C", fg="white", command=lambda: clear(entry1)).pack(pady=5)

tk.Label(root, text="Enter second number:", font=("Arial", 12), bg="#2C3E50", fg="white").pack(pady=5)
entry2 = tk.Entry(root, font=("Arial", 12), width=15)
entry2.pack(pady=5)

# Number Buttons for Second Entry
num_frame2 = tk.Frame(root, bg="#2C3E50")
num_frame2.pack()
for i in range(10):
    tk.Button(num_frame2, text=str(i), font=("Arial", 10), width=3, height=1, bg="#34495E", fg="white",
              command=lambda n=i: press_number(n, entry2)).grid(row=i // 5, column=i % 5, padx=3, pady=3)

# Clear Button for Second Entry
tk.Button(root, text="Clear", font=("Arial", 8), bg="#E74C3C", fg="white", command=lambda: clear(entry2)).pack(pady=5)

# Operator Selection
tk.Label(root, text="Select Operation:", font=("Arial", 14), bg="#2C3E50", fg="yellow").pack(pady=10)

operation_var = tk.StringVar()
operation_var.set("+")

btn_frame = tk.Frame(root, bg="#2C3E50")
btn_frame.pack()

operators = ["+", "-", "*", "/"]
colors = ["#E67E22", "#3498DB", "#2ECC71", "#E74C3C"]

# Adjusting operator button size to make them smaller and handle result directly
for i, op in enumerate(operators):
    tk.Button(btn_frame, text=op, font=("Arial", 11), width=4, height=2, bg=colors[i], fg="white",
              command=lambda o=op: (operation_var.set(o), update_result())).grid(row=0, column=i, padx=5, pady=5)

# Label to display result
result_label = tk.Label(root, text="", font=("Arial", 16), bg="#2C3E50", fg="white")
result_label.pack(pady=20)

# Run application
root.mainloop()
