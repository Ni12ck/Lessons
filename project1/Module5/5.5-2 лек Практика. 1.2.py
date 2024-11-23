# Класс база данных
class Database:
    def __init__(self):
        # Содержит данные в виде пустого словаря
        self.data = {}

    def add_user(self, username, password):
        # Берёт словарь, обращается по ключу пользователя и сохраняет туда значение пароля
        self.data[username] = password


# Класс пользователь
class User:
    """Класс пользователя, содержащий атрибуты: логин и пароль"""

    def __init__(self, username, password, password_confirm):
        """Атрибуты: username - имя пользователя, password - пароль, password_confirm - подтверждение пароля"""
        self.username = username
        # Если пароль совпадает с подтверждением пароля, то тогда задаём этот пароль
        if password == password_confirm: #and str.istitle(password) and (any(ch.isdigit() for ch in password)):
            self.password = password


# Входная точка программы
if __name__ == '__main__':
    # Создал базу данных
    database = Database()
    # Бесконечный цикл создания пользователей
    while True:
        # choice_v = input('Привет! Выбери действие:\n'
        #                  '1 - Вход в аккаунт\n'
        #                  '2 - Регистрация\n')
        user = User(input('Введите логин: '), password1 := input('Введите пароль: '),
                    password2 := input('Подтвердите пароль: '))
        if password1 != password2:
            exit()  # завершение программы
        # моржовый оператор ":=" создаёт переменную, позволяет к ней обращаться, например: print(a := 2)
        database.add_user(user.username, user.password)
        print(database.data)
