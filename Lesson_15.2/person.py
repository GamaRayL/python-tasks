import timeit
from functools import partial


class Person:
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email


class PersonTest:
    __slots__ = ("name", "address", "email")

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email


def get_set_delete(person):
    name = person.name
    address = person.address
    email = person.email

    print(name, address, email)

    person.name = "Avgust"
    person.address = "123 Blabla ul."
    person.email = "month@gmail.com"

    del person.name
    del person.address
    del person.email


def main():
    person = Person("Ivan", "123567 Pushkinskaya ul.", "ivan@mail.ru")
    person_test = PersonTest("Ivan", "123567 Pushkinskaya ul.", "ivan@mail.ru")
    old = min(timeit.repeat(partial(get_set_delete, person), number=1000000))
    new = min(timeit.repeat(partial(get_set_delete, person_test), number=1000000))
    print(f"Текущая реализация: {old}")
    print(f"Тестовая реализация: {new}")
    print(f"Улучшение производительности: {(old - new) / old:.2%}")


if __name__ == "__main__":
    main()
