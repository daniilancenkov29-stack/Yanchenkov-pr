#Дано четырехзначное число. Проверить истинность высказывания: «Данное число читается одинаково слева направо и справа налево».
num = input("Введите четырехзначное число: ")
while type(num) != int:
    try:
        num = int(num)
        if num < 1000 or num > 9999:
            print("Число должно быть четырехзначным!")
            num = input("Введите четырехзначное число: ")
        else:
            break
    except ValueError:
        print("Неправильно ввели!")
        num = input("Введите четырехзначное число: ")
digit1 = num // 1000
digit2 = (num // 100) % 10
digit3 = (num // 10) % 10
digit4 = num % 10
is_palindrome = (digit1 == digit4) and (digit2 == digit3)
print("Число является палиндромом:", is_palindrome)