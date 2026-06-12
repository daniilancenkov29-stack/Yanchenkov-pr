#В матрице найти отрицательные элементы, сформировать из них новый массив. 
#Вывести размер полученного массива
import random
strok = int(input("Введите количество столбцов: "))
stolb = int(input("Введите количество строк: "))
matrix = [[random.randint(-10, 10) for i in range(stolb)] for i in range(strok)]
print("Матрица:", matrix)
negative_elements = list(filter(lambda x: x < 0, [num for strok in matrix for num in strok]))
print("Отрицательные элементы:", negative_elements)
print("Размер массива:", len(negative_elements))





# import random 
# a = int(input('Введите строки'))
# b = int(input('Введите столбцы'))
# matrixa = [random.randint(-15, 15) for g in range(a) for g in range(b)]
# print(matrixa)