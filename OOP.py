#11.1. Создание данных типа "класс"
#Задача 12: Создать класс с двумя полями:

#Поле 1: "Инициалы книги" (например, первые буквы автора и название).
#Поле 2: "Первый тираж" (количество книг в первом тираже).\

class Book:
    def __init__(self, initials, first_print):
        self.initials = initials  # Инициалы книги
        self.first_print = first_print  # Первый тираж

    def display_info(self):
        """Вывод информации о книге."""
        return f"Книга: {self.initials}, Первый тираж: {self.first_print} экземпляров"

book = Book("ЛН", 5000)
print(book.display_info())

#11.2. Наследование классов
#Задача 12: Создать базовый класс с двумя полями и функцию обработки данных, а затем добавить производный класс, который включает дополнительные поля и методы.

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand  
        self.year = year   

    def display_info(self):
        """Вывод базовой информации о транспортном средстве."""
        return f"Марка: {self.brand}, Год выпуска: {self.year}"

class Truck(Vehicle):
    def __init__(self, brand, year, capacity):
        super().__init__(brand, year)
        self.capacity = capacity  # Грузоподъемность

    def display_info(self):
        """Переопределение метода для отображения полной информации."""
        base_info = super().display_info()
        return f"{base_info}, Грузоподъемность: {self.capacity} тонн"

truck = Truck("Volvo", 2018, 20)
print(truck.display_info())

#11.3. Полиморфизм методов класса
#Задача 12: Создать два класса с полиморфным методом, который имеет различное поведение в зависимости от класса.

class Animal:
    def make_sound(self):
        """Полиморфный метод: звук животного."""
        return "Животное издает звук"

class Dog(Animal):
    def make_sound(self):
        """Полиморфный метод: звук собаки."""
        return "Собака лает: Гав-гав!"

class Cat(Animal):
    def make_sound(self):
        """Полиморфный метод: звук кошки."""
        return "Кошка мяукает: Мяу!"

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.make_sound())
