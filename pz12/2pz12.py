# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.
import random
strok = int(input("Введите количество строк: "))
stolb = int(input("Введите количество столбцов: "))
matrix = [[random.randint(0, 20) for i in range(strok)] for i in range(stolb)]
print("Матрица:", matrix)
nechet = list(filter(lambda s: s % 2 != 0, range(len(matrix))))
sred = list(map(lambda s: sum(matrix[s]) / len(matrix[s]), nechet))
print("Среднее арифметическое для строк с нечетным номером:", sred)