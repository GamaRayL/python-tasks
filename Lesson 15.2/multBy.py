from abc import ABC, abstractmethod


class ShowMultBy(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def show_res_for(self, value):
        pass


class MultBy(ShowMultBy):
    """Класс, который использует миксин ShowMultBy."""

    def __init__(self, factor):
        super().__init__()
        self.factor = factor

    def multiply(self, x):
        return x * self.factor

    def show_res_for(self, x):
        result = self.multiply(x)
        print(f"Множитель: {self.factor}, Аргумент: {x}, Результат: {result}")


f = MultBy(10)
f.show_res_for(20)

sh = ShowMultBy()
