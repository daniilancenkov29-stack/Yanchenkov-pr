#Дан список ненулевых целых чисел размера N. Проверить, образуют ли егоэлементы геометрическую прогрессию.
#Если образуют, то вывести знаменатель прогрессии, если нет — вывести 0.
import random

N = int(input("Введите размер списка N: "))
numbers = []
for i in range(N):
    num = random.randint(-50, 50)
    while num == 0:
        num = random.randint(-50, 50)
    numbers.append(num)

print("Исходный список:", numbers)

is_geometric = True
if N > 1:
    if numbers[0] != 0:
        q = numbers[1] / numbers[0]
        for i in range(2, N):
            if numbers[i-1] != 0:
                current_q = numbers[i] / numbers[i-1]
                if abs(current_q - q) > 1e-6:
                    is_geometric = False
                    break
            else:
                is_geometric = False
                break
    else:
        is_geometric = False
else:
    is_geometric = True
    q = 0

if is_geometric and N > 1:
    print("Знаменатель прогрессии:", q)
else:
    print("Результат: 0")