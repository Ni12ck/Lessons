# print(int.__mro__) # (<class 'int'>, <class 'object'>)
# mro() - отображает цепочку наследования для класса, можно увидеть, что в ней присутствует класс Object.
# Это означает, что даже такие базовые типы, как целые числа, наследуются от уже существующего класса.

# print(object)
# класс Object является базовым классом всей иерархии классов

class User:
    __instance = None

    def __new__(cls, *args, **kwargs):
        print('Я в нью')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        print('Я в ините')
        self.args = args
        for key, values in kwargs.items():
            setattr(self, key, values)


other_list = [1, 2, 3, 4, 5]
user_dic = {'name': 'Vladimir', 'age': 29, 'gender': 'male'}

User_1 = User(*other_list, **user_dic)
# User_2 = User()
# print(User.__mro__)
print(User_1.args)
print(User_1.name)
print(User_1.age)
print(User_1.gender)

# print(User_1 is User_2)
