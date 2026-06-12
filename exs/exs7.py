import random
stroki = int(input('Введите строки:'))
stolbcy = int(input('Введите столбцы:'))
matrix = [[random.randint(-15,15) for i in range(stroki)] for i in range(stolbcy)]
print('Матрица:')
for row in matrix:
    formatted_row = [f'{elem:4d}' for elem in row]
    print(''.join(formatted_row))    
count = 0
result = []
for strochka in matrix:
    new_strochka = strochka
    new_strochka.pop(count)
    result += new_strochka
    count += 1 
# for elem in result:
#     print(elem * 2)
print([elem * 2 for elem in result])