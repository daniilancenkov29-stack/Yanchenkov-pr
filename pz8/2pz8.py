#Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16', отражающая продажи продукции по дням в кг. Преобразовать информацию из строки в словари, 
#с использованием функции найти среднее значение продаж по каждому виду продукции, результаты вывести на экран.
sales_str = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
items = sales_str.split()
data = {}
i = 0
while i < len(items):
    product = items[i]
    i += 1
    sales = []
    while i < len(items) and items[i].isdigit():
        sales.append(int(items[i]))
        i += 1
    data[product] = sales
for product, values in data.items():
    avg = sum(values) / len(values)  
    print(f"{product}: средние продажи = {avg}")