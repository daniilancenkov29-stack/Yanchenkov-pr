#Дано множество A из N точек (точки заданы своими координатами x, у). Найти пару различных точек этого множества с максимальным расстоянием между ними и само
#это расстояние (точки выводятся в том же порядке, в котором они перечислены при задании множества A).Расстояние R между точками с координатами
#(x1, y1) и (x2, у2) вычисляется по формуле: R = √(x2 – x1)2 + (у2 – y1)2. Для хранения данных о каждом наборе точек следует использовать по два списка: первый
#список для хранения абсцисс, второй — для хранения ординат.
import random
import math

N = int(input("Введите количество точек N: "))

x_coords = []
y_coords = []

for i in range(N):
    x_coords.append(random.randint(-10, 10))
    y_coords.append(random.randint(-10, 10))

print("Координаты точек:")
for i in range(N):
    print(f"Точка {i+1}: ({x_coords[i]}, {y_coords[i]})")

max_distance = 0
point1_index = -1
point2_index = -1

for i in range(N):
    for j in range(i + 1, N):
        distance = math.sqrt((x_coords[j] - x_coords[i])**2 + (y_coords[j] - y_coords[i])**2)
        if distance > max_distance:
            max_distance = distance
            point1_index = i
            point2_index = j

print("\nПара точек с максимальным расстоянием:")
print(f"Точка 1: ({x_coords[point1_index]}, {y_coords[point1_index]})")
print(f"Точка 2: ({x_coords[point2_index]}, {y_coords[point2_index]})")
print(f"Максимальное расстояние: {max_distance:.2f}")