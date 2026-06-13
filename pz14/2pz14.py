# Вариант 24. С начала суток прошло N секунд (N — целое). Найти количество 
# полных минут, прошедших с начала суток.
import tkinter as tk
from tkinter import messagebox

def calculate_minutes():

    try:
        n = int(entry.get())
        if n < 0:
            messagebox.showerror("Ошибка", "Количество секунд не может быть отрицательным.")
            return
        minutes = n // 60
        label_result.config(text=f"Полных минут: {minutes}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целое число.")

root = tk.Tk()
root.title("Полные минуты с начала суток")
root.geometry("400x200")

label_instruction = tk.Label(root, text="Введите количество секунд N:", font=("Arial", 12))
label_instruction.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), width=20)
entry.pack(pady=5)

button_calc = tk.Button(root, text="Вычислить", command=calculate_minutes, font=("Arial", 12), bg="lightblue")
button_calc.pack(pady=10)

label_result = tk.Label(root, text="Результат: ", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

root.mainloop()