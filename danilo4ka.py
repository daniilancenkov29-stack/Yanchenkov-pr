'''from turtle import *
color("red")
speed(6)
for i in range(4):     
    forward(100)
    left(90)

calories = {'bread': 250, 'milk': 60, 'apple': 52}
product = input("Название продукта: ")
weight = int(input("Вес в граммах: "))
print(f"Каллорийность: {calories[product] * weight * 100} ккал")'''




'''
zarplata = {'Анна': 45000, 'Олег': 60000, 'Игорь': 55000}
zpbolshe = {name: salary for name, salary in zarplata.items() if salary > 50000}
print(zpbolshe)'''

import random
from functools import reduce

a = int(input('Введите количество строк: '))
b = int(input('Введите количество столбцов: '))

# 1. Генерируем матрицу через map (без def)
matrix = list(map(lambda i: list(map(lambda j: random.randint(-10, 10), range(b))), range(a)))

# 2. Выводим матрицу
print("Исходная матрица:")
list(map(lambda row: print(row), matrix))

# 3. Отбираем индексы строк с нечетным номером (индексы: 1, 3, 5...)
odd_indices = list(filter(lambda i: i % 2 != 0, range(a)))

# 4. Для каждой такой строки считаем среднее арифметическое
averages = list(map(lambda i: sum(matrix[i]) / b, odd_indices))

# 5. Выводим результат
print(f"Среднее для строк с нечетным номером (индексы {odd_indices}): {averages}")
'''



















