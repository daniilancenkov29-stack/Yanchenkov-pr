#Даны целые положительные числа N и K. Используя только операции сложения и вычитания, найти частное от деления нацело N на K, а также остаток от этого деления.
N = int(input("N: "))
K = int(input("K: "))
quotient = 0
temp = N
while temp >= K:
    quotient += 1
    temp -= K
print("Частное:", quotient)
print("Остаток:", temp)

n = input("Введите число N: ")
while True:
    try:
        n = int(n)
        break
    except ValueError:
        print("Неправильное число!")
        n = input("Введите число N: ")

summa = 0
i = 1
while i <= n:
    summa += i
    i += 2

print("Сумма нечетных чисел от 1 до", n, ":", summa)