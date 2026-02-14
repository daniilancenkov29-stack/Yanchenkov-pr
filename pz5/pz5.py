#Описать функцию с параметром, которая находит все четные числа от 2 до числа N. Ввод N и отображение результата предусмотреть все функции.
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 1:
            evens.append(i)
    return evens

N = int(input("Введите число N: "))
result = find_even_numbers(N)
print("Четные числа от 0 до", N, ":", result)