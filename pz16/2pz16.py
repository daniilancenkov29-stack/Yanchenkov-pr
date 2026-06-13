''' . Создайте класс "Человек", который содержит информацию о имени, возрасте и поле. 
Создайте классы "Мужчина" и "Женщина", которые наследуются от класса 
"Человек". Каждый класс должен иметь метод, который выводит информацию о 
поле объекта.
'''
class Person:

    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def show_gender(self):
        print(f"Пол: {self.gender}")

    def info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}")

class Man(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Мужчина")

    def show_gender(self):
        print(f"Пол: Мужчина")

class Woman(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Женщина")

    def show_gender(self):
        print(f"Пол: Женщина")

if __name__ == "__main__":
    print("=== Тестирование классов ===")

    person = Person("Алексей", 30, "Мужчина")
    man = Man("Иван", 25)
    woman = Woman("Мария", 28)

    print("\n--- Объект Man ---")
    man.info()
    man.show_gender()

    print("\n--- Объект Woman ---")
    woman.info()
    woman.show_gender()