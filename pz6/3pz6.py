#Дано множество A из N точек (точки заданы своими координатами x, у). Найти пару различных точек этого множества с максимальным расстоянием между ними и само
#это расстояние (точки выводятся в том же порядке, в котором они перечислены при задании множества A).Расстояние R между точками с координатами
#(x1, y1) и (x2, у2) вычисляется по формуле: R = √(x2 – x1)2 + (у2 – y1)2. Для хранения данных о каждом наборе точек следует использовать по два списка: первый
#список для хранения абсцисс, второй — для хранения ординат.
N = int(input("Введите количество точек: "))
x_list = [] 
y_list = [] 
for i in range(N):
    print(f"Точка {i+1}:")
    x = float(input("  Введите x: "))
    y = float(input("  Введите y: "))
    x_list.append(x)
    y_list.append(y)
if N < 2:
    print("Нужно хотя бы 2 точки!")
else:
    max_distance = 0
    point1_index = 0 
    point2_index = 0  
    for i in range(N):
        for j in range(i+1, N):
            x1 = x_list[i]
            y1 = y_list[i]
            x2 = x_list[j]
            y2 = y_list[j]
            distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if distance > max_distance:
                max_distance = distance
                point1_index = i
                point2_index = j
    print("\nРезультат:")
    print(f"Максимальное расстояние: {max_distance}")
    print(f"Точка 1: ({x_list[point1_index]}, {y_list[point1_index]})")
    print(f"Точка 2: ({x_list[point2_index]}, {y_list[point2_index]})")