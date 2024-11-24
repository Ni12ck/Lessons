# Задание "Свой YouTube":
# Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики на тему
# IT (юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса требуются хотя бы базовые
# знания программирования.

# Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут выполнять похожий
# функционал на сайте.

# Всего будет 3 класса: UrTube, Video, User.

# Общее ТЗ:
# Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео,
# авторизации и регистрации пользователя и т.д.


# Подробное ТЗ:

# Каждый объект класса User должен обладать следующими атрибутами и методами:
# 1. Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)

# Каждый объект класса Video должен обладать следующими атрибутами и методами:
# 1. Атрибуты: title(заголовок, строка), duration(продолжительность, секунды),
# time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))

# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
# 1. Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
# 2. Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с
# такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните,
# что password передаётся в виде строки, а сравнивается по хэшу.
# 3. Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
# если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname}
# уже существует". После регистрации, вход выполняется автоматически.
# 4. Метод log_out для сброса текущего пользователя на None.
# 5. Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же
# названием видео ещё не существует. В противном случае ничего не происходит.
# 6. Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое
# слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
# 7. Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то
# ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее
# время просмотра данного видео сбрасывается.

# Для метода watch_video так же учитывайте следующие особенности:
# 1. Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
# 2. Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль
# надпись: "Войдите в аккаунт, чтобы смотреть видео"
# 3. Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
# Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
# 4. После воспроизведения нужно выводить: "Конец видео"


# Код для проверки:
# ur = UrTube()
# v1 = Video('Лучший язык программирования 2024 года', 200)
# v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
# ur.add(v1, v2)

# Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)

# Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')


# Импорт библиотеки time
import time


# Создаю класс User, каждый объект класса User должен обладать следующими атрибутами:
# nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
class User:
    """
    Класс пользователя, содержащий атрибуты: имя пользователя, пароль, возраст
    """

    def __init__(self, nickname: str, password: int, age: int):
        # nickname(имя пользователя, строка)
        self.nickname = nickname
        # password(в хэшированном виде, число)
        self.password = hash(password)
        # age(возраст, число)
        self.age = age


# Создаю класс Video, каждый объект класса Video должен обладать следующими атрибутами:
# title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)),
# adult_mode(ограничение по возрасту, bool (False по умолчанию))
class Video:
    """
    Класс видео, содержащий атрибуты: заголовок, продолжительность
    """

    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        # title(заголовок, строка)
        self.title = title
        # duration(продолжительность, секунды)
        self.duration = duration
        # time_now(секунда остановки (изначально 0))
        self.time_now = time_now
        # adult_mode(ограничение по возрасту, bool (False по умолчанию))
        self.adult_mode = adult_mode

    # функция для будущего поиска по названию
    def __str__(self):
        return self.title


# Создаю класс UrTube, каждый объект класса UrTube должен обладать следующими атрибутами и методами:
# users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
class UrTube:
    """
    Класс UrTube, содержащий атрибуты: список пользователей, список видео, текущий пользователь
    """

    def __init__(self, users, videos, current_user):
        # users(список объектов User)
        self.users = []
        # videos(список объектов Video)
        self.videos = []
        #  current_user(текущий пользователь, User)
        self.current_user = None

    # Создал метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users
    # с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Тут
    # password передаётся в виде строки, а сравнивается по хэшу.
    def log_in(self, nickname, password):
        hash_password = hash(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hash_password:
                self.current_user = user

    # Создал метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в
    # список, если пользователя не существует (с таким же nickname). Если существует, выводит на экран:
    # "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print('Пользователь {nickname} уже существует')
            else:
                self.users.append(User(nickname, password, age))

    # Создал метод log_out для сброса текущего пользователя на None.
    def log_out(self):
        self.current_user = None

    # Создал метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если
    # с таким же названием видео ещё не существует. В противном случае ничего не происходит.
    def add(self, *videos):
        for video in videos:
            if str(video) not in self.videos:
                self.videos.append(video)

    # Создал метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих
    # поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
    def get_videos(self, search_word):
        search_word = str(search_word).lower()
        # список названий всех видео, содержащих поисковое слов
        list_after_search = []
        for video in self.videos:
            if search_word in video.title.lower():
                list_after_search.append(str(video))
        return list_after_search

    # Создал метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до
    # пробела), то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся
    # просмотр. После текущее время просмотра данного видео сбрасывается.
    # Для метода watch_video так же учёл следующие особенности:
    # 1. Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
    # 2. Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить
    # в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
    # 3. Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения
    # 18+.
    # Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
    # 4. После воспроизведения нужно выводить: "Конец видео"
    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for second in range(video.time_now, video.duration):
                    print(second)
                    time.sleep(1)
                print("Конец видео")
                video.time_now = 0
                return

# Входная точка программы
if __name__ == '__main__':

    # Код для проверки:
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')