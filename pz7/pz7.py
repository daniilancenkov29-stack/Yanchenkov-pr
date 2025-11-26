text = input("Введите строку: ")
words = text.split()
count = 0

for word in words:
    if word.count('А') == 3:
        count += 1

print("Количество слов с тремя буквами 'А':", count)