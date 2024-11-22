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
        if password == password_confirm:
            self.password = password

# Входная точка программы
if __name__ == '__main__':
    # Создал базу данных
    database = Database()
    user = User(input('Введите логин: '), input('Введите пароль: '), input('Подтвердите пароль: '))
    database.add_user(user.username, user.password)