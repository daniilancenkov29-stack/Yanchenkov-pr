import random

# Task 1
seq1 = [random.randint(-30, 30) for _ in range(15)]
seq2 = [random.randint(-30, 30) for _ in range(15)]

with open("first_sequence.txt", "w", encoding="utf-8") as f1:
    f1.write("Содержимое первого файла:\n")
    f1.write(" ".join(map(str, seq1)) + "\n\n")
    multiples_of_3 = [x for x in seq1 if x % 3 == 0]
    f1.write("Элементы кратные 3:\n")
    f1.write(" ".join(map(str, multiples_of_3)) + "\n\n")
    product = 1
    for num in seq1:
        product *= num
    f1.write("Произведение элементов:\n")
    f1.write(str(product) + "\n\n")
    f1.write("Минимальный элемент:\n")
    f1.write(str(min(seq1)) + "\n")

with open("second_sequence.txt", "w", encoding="utf-8") as f2:
    f2.write("Содержимое второго файла:\n")
    f2.write(" ".join(map(str, seq2)) + "\n\n")
    multiples_of_5 = [x for x in seq2 if x % 5 == 0]
    f2.write("Элементы кратные 5:\n")
    f2.write(" ".join(map(str, multiples_of_5)) + "\n\n")
    f2.write("Количество элементов:\n")
    f2.write(str(len(seq2)) + "\n\n")
    mean = sum(seq2) / len(seq2)
    f2.write("Среднее арифметическое элементов:\n")
    f2.write(str(mean) + "\n")
