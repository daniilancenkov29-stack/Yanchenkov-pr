# Извлеките из числа две первые цифры
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