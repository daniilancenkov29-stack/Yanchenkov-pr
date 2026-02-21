chetverg = {"bread": 250, "milk": 60, "apple": 52}
product = str(input("введите название продукта"))
weight = int(input("введите вес продукта в граммах"))
if product in chetverg:
    x = weight * chetverg[product]/100
    print(x)
else:
    print("продукта нет")    