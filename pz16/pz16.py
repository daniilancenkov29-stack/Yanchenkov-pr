'''. Создайте класс "Компьютер" с атрибутами "марка", "процессор" и "оперативная 
память". Напишите метод, который выводит информацию о компьютере в формате 
"Марка: марка, Процессор: процессор, Оперативная память: память".'''

class Computer:
    def __init__(self, brand: str, processor: str, ram: str):
        self.brand = brand
        self.processor = processor
        self.ram = ram

    def display_info(self):
        print(f"Марка: {self.brand}, Процессор: {self.processor}, Оперативная память: {self.ram}")

if __name__ == "__main__":
    print("=== Тестирование класса Computer ===\n")

    comp1 = Computer("Apple MacBook Pro", "Apple M2", "16 ГБ")
    comp2 = Computer("Dell XPS 13", "Intel Core i7-1360P", "32 ГБ")
    comp3 = Computer("ASUS ROG", "AMD Ryzen 9 7945HX", "64 ГБ")

    print("Компьютер 1:")
    comp1.display_info()

    print("\nКомпьютер 2:")
    comp2.display_info()

    print("\nКомпьютер 3:")
    comp3.display_info()