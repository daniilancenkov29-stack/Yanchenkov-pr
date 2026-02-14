import random
A = [random.randint(-50, 100) for _ in range(10)]
print(f"Список A: {A}")
B = [x for x in A if x < 0 and x % 7 == 0]
print(f"Список B: {B}")
count_B = len(B)
summ_B = []
print(f"Количество чисел в списке B и сумма: {count_B}, {sum(B)}")
