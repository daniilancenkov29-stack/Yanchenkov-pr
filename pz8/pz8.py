#Найдите ключ с минимальным значением в sample_dict = {'Physics': 82, 'Math': 65, 'history': 75}.
sample_dict = {'Physics': 82, 'Math': 65, 'history': 75}
min_key = max(sample_dict, key=sample_dict.get)
print("Исходный словарь:", sample_dict)
print("Ключ с минимальным значением:", min_key)