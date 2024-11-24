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
        if password == password_confirm:  # len(password) >= 8 and str.istitle(password) and (any(ch.isdigit() for ch in password)) :
            self.password = password


# Входная точка программы
if __name__ == '__main__':
    # Создал базу данных
    database = Database()
    # Бесконечный цикл создания пользователей
    while True:
        choice_v = int(input('Привет! Выбери действие: \n1 - Вход в аккаунт\n2 - Регистрация\n'))
        # Если пользователь выбрал вход в аккаунт
        if choice_v == 1:
            # переменная связанная с логином
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            # Если логин находится в словаре с данными
            if login in database.data:
                # сравнение введённого пароля с паролем в бд под ключом данного пользователя
                if password == database.data[login]:
                    print(f'{login}, Вы вошли в аккаунт ')
                    # завершение работы
                    break
                else:
                    print('Вы ввели неверный пароль')
            else:
                print('Пользователь не найден')
        # Если пользователь выбрал регистрацию
        if choice_v == 2:
            # моржовый оператор ":=" создаёт переменную, позволяет к ней обращаться, например: print(a := 2)
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                        password2 := input('Подтвердите пароль: '))
            if password != password2:
                print('Введённые пароли не совпадают, попробуйте снова')
                continue # переход к началу цикла
            database.add_user(user.username, user.password)
        print(database.data)
        print()
