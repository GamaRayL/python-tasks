class TodoList:
    def __init__(self, data_lst):
        self.data = data_lst

    def __repr__(self):
        data_type = self.data.__class__.__name__
        cls_name = self.__class__.__name__
        value_types = ",".join(set(type(item).__name__ for item in self.data))

        return f"{cls_name}({data_type}[{value_types}])"

    def __str__(self):
        values = "\n".join(item for item in self.data)
        return values

    def __add__(self, other):
        self.combine_data = self.data + other.data
        return TodoList(self.combine_data)

    def __len__(self):
        return len(self.data)


tasks = ['task1', "task2"]

list1 = TodoList(tasks)

print(repr(list1))
# TodoList(list[str])

print(list1)
# task1
# task2


list2 = TodoList(['task3', 'task4'])

list3 = list1 + list2

print(list3)
# task1
# task2
# task3
# task4

print(len(list3))
