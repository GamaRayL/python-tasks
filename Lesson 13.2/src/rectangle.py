from datetime import date


class Rectangle:
    def __init__(self, width: int, length: int):
        self.width = width
        self.length = length

    def perimeter(self):
        return (self.width + self.length) * 2

    def area(self):
        return self.width * self.length

    def display(self):
        print(f"Длина: {self.width}\n"
              f"Ширина: {self.length}\n"
              f"Периметр: {self.perimeter()}\n"
              f"Площадь: {self.area()}")


# example = Rectangle(10, 10)
# example.display()


class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def display(self):
        print(f"{self.__name}. Возраст: {self.__age}")

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, str):
            raise ValueError("Возраст задаётся в формате int или float")
        elif 0 < value < 120:
            self.__age = value
        else:
            raise ValueError("Возраст должен быть больше 0 и меньше 120")

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("Имя должно быть в формате str")

    @classmethod
    def from_birth_year(cls, name: str, year: int):
        age = date.today().year - year
        return cls(name, age)


person = Person("Иван", 19)
person.display()

person1 = Person.from_birth_year('Николай', 2000)
person1.display()
