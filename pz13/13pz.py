#В исходном текстовом файле(Dostoevsky.txt) найти все годы деятельности писателя 
#(например, 1821 года, 1837 год, 1843 году и так далее по всему тексту). Посчитать 
#количество полученных элементов.
import re

with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()

pattern = '\\b(\\d{4})(?:[–\\-](\\d{4}))?\\s*(год(?:а|у)?|гг?\\.?)'

matches = re.findall(pattern, text)

print("Найденные годы деятельности писателя:")

for start, end, suffix in matches:
    if end:
        print(f"  {start}–{end} {suffix}")
    else:
        print(f"  {start} {suffix}")

print(f"\nВсего элементов: {len(matches)}")