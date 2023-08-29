from src.category import Category


class Store:
    def __init__(self, categories):
        self.__categories = categories

    @property
    def categories(self):
        tmp = []
        for cat in self.__categories:
            tmp.append(cat) if cat.is_active else None

        return tmp
