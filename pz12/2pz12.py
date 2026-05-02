# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее 
#элементов.
import random
matrix = [[random.randint(0, 20) for _ in range(4)] for _ in range(3)]
print("Матрица:", matrix)
odd_rows = list(filter(lambda i: i % 2 != 0, range(len(matrix))))
averages = list(map(lambda i: sum(matrix[i]) / len(matrix[i]), odd_rows))
print("Среднее арифметическое для строк с нечетным номером:", averages)