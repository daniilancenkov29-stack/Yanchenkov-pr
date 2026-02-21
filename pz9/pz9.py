"""
В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
мясо, молоко, сыр. Определить:
1. какие товары из Магнита, отсутствуют в Пятерочке.
2. какие товары из Пятерочки, отсутствуют в Магните
3. полный перечень всех товаров.
4. равны ли перечни товаров
"""
magnit = set("Молоко, соль, сахар".lower().replace(",", "").split())
pyaterka = set("мясо, молоко, сыр".lower().replace(",", "").split())

print("1. товары из магнита, которых нет в пятерочке:")
for tovar in magnit - pyaterka:
    print("-", tovar)

print("\n2. товары из пятерочки, которых нету в магните:")
for tovar in pyaterka - magnit:
    print("-", tovar)

print("\n3. перечень всех товаров:")

vse_tovary = set()

for tovar in magnit:
    vse_tovary.add(tovar)

for tovar in pyaterka:
    vse_tovary.add(tovar)

for tovar in vse_tovary:
    print("-", tovar)

print("\n4. равны ли перечни товаров?:")
if magnit == pyaterka:
    print("Да")
else:
    print("нет")