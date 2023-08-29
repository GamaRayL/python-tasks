class MyList(list):
    def __new__(cls, *args, **kwargs):
        print('Работает магический метод')
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, value):
        print('Работает магический метод')
        super().__init__(value)

    def __getitem__(self, item):
        print('Работает магический метод')
        return super().__getitem__(item)

    def __str__(self):
        print('Работает магический метод')
        return super().__str__()

    def __len__(self):
        print('Работает магический метод')
        return super().__len__()


lst = MyList(['Jone', 'Snow', 'Java'])

if not lst[2] == 'Python':
    lst[2] = 'Python'

print(lst)
print(len(lst))
