from tkinter import *
from tkinter import ttk, messagebox
import random

root = Tk()
root.title("Опрос – Янченков интернет")
root.geometry("550x650")

f = ttk.Frame(root, padding="20")
f.pack()

Label(f, text="Форма регистрации пользователя", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(0,15))

name = Entry(f, width=30)
pwd = Entry(f, width=30, show="*")
age = Spinbox(f, from_=0, to=150, width=28)

for i, (label, widget) in enumerate([("Имя:", name), ("Пароль:", pwd), ("Возраст:", age)], 1):
    Label(f, text=label).grid(row=i, column=0, sticky="w", pady=3)
    widget.grid(row=i, column=1, padx=(20,0), pady=3)

Label(f, text="Пол:").grid(row=4, column=0, sticky="nw", pady=3)
gender_frame = Frame(f)
gender_frame.grid(row=4, column=1, padx=(20,0))
gender_var = StringVar()
Radiobutton(gender_frame, text="Мужской", var=gender_var, value="Мужской").pack(anchor="w")
Radiobutton(gender_frame, text="Женский", var=gender_var, value="Женский").pack(anchor="w")

Label(f, text="Увлечения:").grid(row=5, column=0, sticky="nw", pady=3)
hobby_frame = Frame(f)
hobby_frame.grid(row=5, column=1, padx=(20,0))
music = BooleanVar()
video = BooleanVar()
draw = BooleanVar()
Checkbutton(hobby_frame, text="Музыка", var=music).pack(anchor="w")
Checkbutton(hobby_frame, text="Видео", var=video).pack(anchor="w")
Checkbutton(hobby_frame, text="Рисование", var=draw).pack(anchor="w")

Label(f, text="Страна:").grid(row=6, column=0, sticky="w", pady=3)
country = ttk.Combobox(f, values=["Россия","Украина","Беларусь","Казахстан"], width=21)
country.grid(row=6, column=1, padx=(20,0), pady=3)

Label(f, text="Город:").grid(row=7, column=0, sticky="w", pady=3)
city = Entry(f, width=30)
city.grid(row=7, column=1, padx=(20,0), pady=3)

Label(f, text="О себе:").grid(row=8, column=0, sticky="nw", pady=3)
about = Text(f, width=30, height=3)
about.grid(row=8, column=1, padx=(20,0), pady=3)
about.insert("1.0", "краткая информация о ваших увлечениях")

Label(f, text="Решите пример:").grid(row=9, column=0, columnspan=2, sticky="w", pady=(10,0))
num1, num2 = random.randint(1,10), random.randint(1,10)
Label(f, text=f"{num1} + {num2} = ?").grid(row=10, column=0, padx=(20,0))
captcha = Entry(f, width=10)
captcha.grid(row=10, column=1, sticky="w", padx=(20,0))

def clear_form():
    name.delete(0, END)
    pwd.delete(0, END)
    age.delete(0, END)
    age.insert(0, "0")
    gender_var.set("")
    music.set(0)
    video.set(0)
    draw.set(0)
    country.set("")
    city.delete(0, END)
    about.delete("1.0", END)
    about.insert("1.0", "краткая информация о ваших увлечениях")
    captcha.delete(0, END)

def submit_form():
    try:
        if int(captcha.get()) != num1 + num2:
            messagebox.showerror("Ошибка", f"Неверно! {num1}+{num2}={num1+num2}")
            return
    except:
        messagebox.showerror("Ошибка", "Введите число")
        return
    if not name.get():
        messagebox.showwarning("Ошибка", "Введите имя")
        return
    hobbies = []
    for text, var in [("Музыка", music), ("Видео", video), ("Рисование", draw)]:
        if var.get():
            hobbies.append(text)
    messagebox.showinfo("Готово", f"Имя: {name.get()}\nВозраст: {age.get()}\nПол: {gender_var.get()}\nУвлечения: {', '.join(hobbies)}")

Button(f, text="Отменить ввод", command=clear_form, bg="#f0f0f0", width=15).grid(row=11, column=0, pady=20)
Button(f, text="Данные подтверждаю", command=submit_form, bg="#4CAF50", fg="white", width=18).grid(row=11, column=1)

root.mainloop()