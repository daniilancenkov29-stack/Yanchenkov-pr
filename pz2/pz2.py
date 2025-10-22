# Извлеките из числа две первые цифры
try:
    n=int(input("Введите число:"))
    first_digit = n // 10
    second_digit = n % 10
    print(f"Две первые цифры:{first_digit} и {second_digit}")
except ValueError:
    print("Это не число")