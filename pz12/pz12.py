#В матрице найти отрицательные элементы, сформировать из них новый массив. 
#Вывести размер полученного массива
import random
matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(3)]
print("Матрица:", matrix)
negative_elements = list(filter(lambda x: x < 0, [num for row in matrix for num in row]))
print("Отрицательные элементы:", negative_elements)
print("Размер массива:", len(negative_elements))

