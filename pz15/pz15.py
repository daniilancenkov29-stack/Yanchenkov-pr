"""Вариант 24
Приложение ВЫДАЧА КРЕДИТОВ для некоторой организации. БД должна 
содержать таблицу Клиент со следующей структурой записи: ФИО клиента, ФИО 
сотрудника банка, срок кредита, процент кредита, сумма кредита.
"""
import sqlite3 as sq

with sq.connect('credits.db') as con:
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Client (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fio_client TEXT NOT NULL,
            fio_employee TEXT NOT NULL,
            credit_term INTEGER NOT NULL,
            credit_percent REAL NOT NULL,
            credit_amount REAL NOT NULL
        )
    """)

    cur.execute("DELETE FROM Client")

    clients_data = [
        ('Иванов И.И.', 'Петрова А.В.', 12, 8.5, 100000),
        ('Петров П.П.', 'Сидоров Д.М.', 24, 9.0, 250000),
        ('Сидоров С.С.', 'Иванова Е.Н.', 36, 10.2, 500000),
        ('Кузнецова А.А.', 'Смирнов В.В.', 60, 11.0, 1200000),
        ('Смирнов Д.Д.', 'Кузнецова Л.И.', 18, 7.8, 75000),
        ('Васильева О.В.', 'Петрова А.В.', 30, 9.5, 300000),
        ('Николаев Н.Н.', 'Сидоров Д.М.', 48, 10.8, 800000),
        ('Михайлова М.М.', 'Иванова Е.Н.', 12, 8.0, 45000),
        ('Алексеев А.А.', 'Смирнов В.В.', 24, 9.9, 620000),
        ('Егорова Е.Е.', 'Кузнецова Л.И.', 36, 10.5, 950000)
    ]

    cur.executemany("INSERT INTO Client (fio_client, fio_employee, credit_term, credit_percent, credit_amount) VALUES (?, ?, ?, ?, ?)", clients_data)
    print("Добавлено 10 записей.\n")

print("--- ПОИСК ---")
with sq.connect('credits.db') as con:
    cur = con.cursor()
    print("1 - поиск по ФИО клиента")
    print("2 - поиск по сотруднику и сумме кредита >= заданной")
    print("3 - поиск по сроку кредита в диапазоне")
    choice = input("Выберите вариант: ")

    if choice == '1':
        fio = input("Введите ФИО клиента: ")
        cur.execute("SELECT * FROM Client WHERE fio_client = ?", (fio,))
        for row in cur.fetchall():
            print(row)
    elif choice == '2':
        employee = input("Введите ФИО сотрудника: ")
        min_sum = float(input("Минимальная сумма кредита: "))
        cur.execute("SELECT * FROM Client WHERE fio_employee = ? AND credit_amount >= ?", (employee, min_sum))
        for row in cur.fetchall():
            print(row)
    elif choice == '3':
        ot = int(input("Срок от (мес): "))
        do = int(input("Срок до (мес): "))
        cur.execute("SELECT * FROM Client WHERE credit_term BETWEEN ? AND ?", (ot, do))
        for row in cur.fetchall():
            print(row)
    else:
        print("Неверный выбор")

print("\n--- УДАЛЕНИЕ ---")
with sq.connect('credits.db') as con:
    cur = con.cursor()
    print("1 - удалить по id")
    print("2 - удалить по сотруднику")
    print("3 - удалить со сроком кредита > N")
    choice = input("Выберите вариант: ")

    if choice == '1':
        uid = int(input("Введите id: "))
        cur.execute("DELETE FROM Client WHERE id = ?", (uid,))
        print("Удалено записей:", cur.rowcount)
    elif choice == '2':
        employee = input("Введите ФИО сотрудника: ")
        cur.execute("DELETE FROM Client WHERE fio_employee = ?", (employee,))
        print("Удалено записей:", cur.rowcount)
    elif choice == '3':
        months = int(input("Срок кредита больше (мес): "))
        cur.execute("DELETE FROM Client WHERE credit_term > ?", (months,))
        print("Удалено записей:", cur.rowcount)
    else:
        print("Неверный выбор")

print("\n--- РЕДАКТИРОВАНИЕ ---")
with sq.connect('credits.db') as con:
    cur = con.cursor()
    print("1 - изменить процент кредита по id")
    print("2 - изменить сумму кредита по ФИО клиента")
    print("3 - изменить срок кредита по ФИО сотрудника")
    choice = input("Выберите вариант: ")

    if choice == '1':
        uid = int(input("Введите id: "))
        new_percent = float(input("Новый процент: "))
        cur.execute("UPDATE Client SET credit_percent = ? WHERE id = ?", (new_percent, uid))
        print("Обновлено записей:", cur.rowcount)
    elif choice == '2':
        fio = input("Введите ФИО клиента: ")
        new_amount = float(input("Новая сумма кредита: "))
        cur.execute("UPDATE Client SET credit_amount = ? WHERE fio_client = ?", (new_amount, fio))
        print("Обновлено записей:", cur.rowcount)
    elif choice == '3':
        employee = input("Введите ФИО сотрудника: ")
        new_term = int(input("Новый срок кредита (мес): "))
        cur.execute("UPDATE Client SET credit_term = ? WHERE fio_employee = ?", (new_term, employee))
        print("Обновлено записей:", cur.rowcount)
    else:
        print("Неверный выбор")

print("\n--- ВСЕ ЗАПИСИ ПОСЛЕ ИЗМЕНЕНИЙ ---")
with sq.connect('credits.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Client")
    for row in cur.fetchall():
        print(row)