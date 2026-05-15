#В матрице найти отрицательные элементы, сформировать из них новый массив. 
#Вывести размер полученного массива
import random
strok = int(input("Введите количество строк: "))
stolb = int(input("Введите количество столбцов: "))
matrix = [[random.randint(-10, 10) for i in range(strok)] for i in range(stolb)]
print("Матрица:", matrix)
negative_elements = list(filter(lambda x: x < 0, [num for strok in matrix for num in strok]))
print("Отрицательные элементы:", negative_elements)
print("Размер массива:", len(negative_elements))
