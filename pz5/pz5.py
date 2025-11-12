def print_line(n):
    s = ''
    for i in range(n):
        s += '*'
    print(s)

n = input("Введите число символов: ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Ошибка!")
        n = input("Введите число символов: ")

print_line(n)