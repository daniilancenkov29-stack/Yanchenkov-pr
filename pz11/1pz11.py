'''Составить список, в который будут включены только согласные буквы и привести 
их к верхнему регистру. Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 
'Каир'].'''

'''
cities = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
glasnye = ('аеёиоуыэюяАЕЁИОУЫЭЮЯ')
consonants_upper = list(map(
    str.upper,
    filter(
        lambda c: c not in glasnye,
        [char for city in cities for char in city]
    )
))
print(consonants_upper)'''


'''Создать cписок A на 10 случайных элементов. Создать список B из чисел списка A, меньших 0 и кратных 5. Найти количество чисел списка B'''
import random
A = list(map(lambda _: random.randint(-50, 50), range(10)))
print("Список A:", A)
B = list(filter(lambda x: x < 0 and x % 5 == 0, A))
print("Список B (отрицательные числа, кратные 5):", B)
