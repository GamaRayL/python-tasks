class Employee:
    raise_coef = 1.4

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay

    def raise_pay(self):
        self.pay *= self.raise_coef


class Developer(Employee):
    raise_coef = 1.1

    def __init__(self, name, surname, pay, pro_lang):
        super().__init__(name, surname, pay)
        self.pro_lang = pro_lang


dev1 = Developer("Ivan", "Ivanov", 100000, "python")
dev1.raise_pay()
print(dev1.__dict__)
