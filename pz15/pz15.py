"""
Практическое занятие № 15, Вариант 24
Приложение "ВЫДАЧА КРЕДИТОВ"
Работа с однотабличной БД (Клиент).
Функции: добавление (10 записей), поиск, удаление, редактирование.
Каждая операция имеет по 3 варианта SQL-запроса.
"""

import sqlite3
import os


DB_NAME = "credits.db"
TABLE_NAME = "Client"


def get_db_connection():
    """Устанавливает соединение с БД и включает поддержку внешних ключей."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Доступ к колонкам по имени
    return conn


def create_table():
    """Создаёт таблицу Client, если она не существует."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fio_client TEXT NOT NULL,
            fio_employee TEXT NOT NULL,
            credit_term INTEGER NOT NULL,  -- срок кредита в месяцах
            credit_percent REAL NOT NULL,   -- процент кредита (например, 12.5)
            credit_amount REAL NOT NULL     -- сумма кредита
        )
    """)
    conn.commit()
    conn.close()


def clear_table():
    """Очищает таблицу перед добавлением свежих 10 записей (опционально)."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {TABLE_NAME}")
    conn.commit()
    conn.close()


def add_initial_records():
    """Добавляет ровно 10 записей в БД."""
    records = [
        ("Иванов И.И.", "Петрова А.В.", 12, 8.5, 100000),
        ("Петров П.П.", "Сидоров Д.М.", 24, 9.0, 250000),
        ("Сидоров С.С.", "Иванова Е.Н.", 36, 10.2, 500000),
        ("Кузнецова А.А.", "Смирнов В.В.", 60, 11.0, 1200000),
        ("Смирнов Д.Д.", "Кузнецова Л.И.", 18, 7.8, 75000),
        ("Васильева О.В.", "Петрова А.В.", 30, 9.5, 300000),
        ("Николаев Н.Н.", "Сидоров Д.М.", 48, 10.8, 800000),
        ("Михайлова М.М.", "Иванова Е.Н.", 12, 8.0, 45000),
        ("Алексеев А.А.", "Смирнов В.В.", 24, 9.9, 620000),
        ("Егорова Е.Е.", "Кузнецова Л.И.", 36, 10.5, 950000),
    ]
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.executemany(f"""
        INSERT INTO {TABLE_NAME} (fio_client, fio_employee, credit_term, credit_percent, credit_amount)
        VALUES (?, ?, ?, ?, ?)
    """, records)
    conn.commit()
    conn.close()
    print("✓ Добавлено 10 начальных записей в таблицу.")


def show_all_records():
    """Выводит все записи из таблицы."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    rows = cursor.fetchall()
    conn.close()
    if not rows:
        print("Таблица пуста.")
        return
    print("\n--- Все записи ---")
    for row in rows:
        print(f"ID:{row['id']} | Клиент:{row['fio_client']} | Сотрудник:{row['fio_employee']} | "
              f"Срок(мес):{row['credit_term']} | Процент:{row['credit_percent']}% | Сумма:{row['credit_amount']}")
    print("-----------------\n")


def search_records():
    """
    Поиск записей с 3 вариантами условий.
    """
    print("\n--- Поиск записей ---")
    print("Выберите тип поиска:")
    print("1. По ФИО клиента (точное совпадение)")
    print("2. По сотруднику банка и минимальной сумме кредита")
    print("3. По сроку кредита в диапазоне (от и до)")
    choice = input("Ваш выбор (1/2/3): ").strip()

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        if choice == "1":
            fio = input("Введите ФИО клиента для поиска: ").strip()
            cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE fio_client = ?", (fio,))
        elif choice == "2":
            employee = input("Введите ФИО сотрудника: ").strip()
            min_sum = float(input("Минимальная сумма кредита: "))
            cursor.execute(f"""
                SELECT * FROM {TABLE_NAME} 
                WHERE fio_employee = ? AND credit_amount >= ?
            """, (employee, min_sum))
        elif choice == "3":
            term_min = int(input("Срок кредита от (мес): "))
            term_max = int(input("Срок кредита до (мес): "))
            cursor.execute(f"""
                SELECT * FROM {TABLE_NAME} 
                WHERE credit_term BETWEEN ? AND ?
            """, (term_min, term_max))
        else:
            print("Неверный выбор.")
            conn.close()
            return

        rows = cursor.fetchall()
        conn.close()
        if rows:
            for row in rows:
                print(f"ID:{row['id']} | {row['fio_client']} | {row['fio_employee']} | "
                      f"{row['credit_term']} мес | {row['credit_percent']}% | {row['credit_amount']}")
        else:
            print("Записи не найдены.")
    except Exception as e:
        print(f"Ошибка при поиске: {e}")
        conn.close()


def delete_records():
    """
    Удаление записей с 3 вариантами условий.
    """
    print("\n--- Удаление записей ---")
    print("Выберите тип удаления:")
    print("1. Удалить по ID")
    print("2. Удалить все записи для конкретного сотрудника")
    print("3. Удалить записи с кредитом более N месяцев")
    choice = input("Ваш выбор (1/2/3): ").strip()

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        if choice == "1":
            record_id = int(input("Введите ID записи для удаления: "))
            cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = ?", (record_id,))
        elif choice == "2":
            employee = input("Введите ФИО сотрудника: ")
            cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE fio_employee = ?", (employee,))
        elif choice == "3":
            months = int(input("Удалить записи со сроком кредита более (мес): "))
            cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE credit_term > ?", (months,))
        else:
            print("Неверный выбор.")
            conn.close()
            return

        conn.commit()
        deleted = cursor.rowcount
        conn.close()
        print(f"✓ Удалено записей: {deleted}")
    except Exception as e:
        print(f"Ошибка при удалении: {e}")
        conn.close()


def edit_records():
    """
    Редактирование записей с 3 вариантами условий.
    """
    print("\n--- Редактирование записей ---")
    print("Выберите, какие записи редактировать:")
    print("1. По ID (изменить процент кредита)")
    print("2. По ФИО клиента (изменить сумму кредита)")
    print("3. По ФИО сотрудника (изменить срок кредита)")
    choice = input("Ваш выбор (1/2/3): ").strip()

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        if choice == "1":
            record_id = int(input("Введите ID записи: "))
            new_percent = float(input("Новый процент кредита: "))
            cursor.execute(f"UPDATE {TABLE_NAME} SET credit_percent = ? WHERE id = ?", (new_percent, record_id))
        elif choice == "2":
            fio_client = input("Введите ФИО клиента: ")
            new_amount = float(input("Новая сумма кредита: "))
            cursor.execute(f"UPDATE {TABLE_NAME} SET credit_amount = ? WHERE fio_client = ?", (new_amount, fio_client))
        elif choice == "3":
            fio_employee = input("Введите ФИО сотрудника: ")
            new_term = int(input("Новый срок кредита (месяцы): "))
            cursor.execute(f"UPDATE {TABLE_NAME} SET credit_term = ? WHERE fio_employee = ?", (new_term, fio_employee))
        else:
            print("Неверный выбор.")
            conn.close()
            return

        conn.commit()
        updated = cursor.rowcount
        conn.close()
        print(f"✓ Обновлено записей: {updated}")
    except Exception as e:
        print(f"Ошибка при редактировании: {e}")
        conn.close()


def main():
    """Главная функция программы."""
    print("=== Приложение ВЫДАЧА КРЕДИТОВ (Вариант 24) ===")

    # Инициализация БД
    create_table()
    # Очистка и добавление 10 записей (чтобы каждый запуск был с чистыми данными)
    clear_table()
    add_initial_records()

    while True:
        print("\nМеню:")
        print("1. Показать все записи")
        print("2. Поиск записей (3 варианта)")
        print("3. Удаление записей (3 варианта)")
        print("4. Редактирование записей (3 варианта)")
        print("5. Выход")
        cmd = input("Выберите действие: ").strip()

        if cmd == "1":
            show_all_records()
        elif cmd == "2":
            search_records()
        elif cmd == "3":
            delete_records()
        elif cmd == "4":
            edit_records()
        elif cmd == "5":
            print("Работа завершена.")
            break
        else:
            print("Неверная команда, попробуйте снова.")


if __name__ == "__main__":
    main()