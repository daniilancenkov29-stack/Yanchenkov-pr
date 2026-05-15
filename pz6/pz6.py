#Дан список ненулевых и целых чисел размера N. Проверить, образуют ли его элементы геометрическую прогрессию.
#Если образуют, то вывести знаменатель прогрессии, если нет — вывести 0.
N = int(input("Введите количество чисел: "))
numbers = []
for i in range(N):
    num = int(input(f"Введите число {i+1}: "))
    numbers.append(num)
if N < 2:
    print("Нужно хотя бы 2 числа")
else:
    znamenatel = numbers[1] / numbers[0]
    is_progressiya = True
    
    for i in range(1, N):
        if numbers[i] != numbers[i-1] * znamenatel:
            is_progressiya = False
            break
    if is_progressiya:
        print(f"Это геометрическая прогрессия. Знаменатель: {znamenatel}")
    else:
        print("Это не геометрическая прогрессия. Знаменатель: 0")
