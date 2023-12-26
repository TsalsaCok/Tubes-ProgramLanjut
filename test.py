import tkinter as tk
from tkinter import messagebox

def calculate_average():
    try:
        numbers_str = entry_numbers.get()
        numbers = [float(num) for num in numbers_str.split(",")]

        if not numbers:
            raise ValueError("Please enter valid numbers.")

        average = sum(numbers) / len(numbers)
        messagebox.showinfo("Result", f"Rata-ratanya adalah = {average:.2f}")

    except ValueError as ve:
        messagebox.showerror("Error", str(ve))

# GUI setup
root = tk.Tk()
root.title("Average Calculator")

# Entry widget for numbers input
label_numbers = tk.Label(root, text="Masukkan Angka (yang dipisahkan oleh tanda koma):")
label_numbers.pack(pady=10)
entry_numbers = tk.Entry(root, width=50)
entry_numbers.pack(pady=50)

# Button to calculate average
calculate_button = tk.Button(root, text="Hitung Rata-rata", command=calculate_average)
calculate_button.pack(pady=20)

# Run the GUI
root.mainloop()