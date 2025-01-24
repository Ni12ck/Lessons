# В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.

# Изменения в классе Runner:
# 1. Появился атрибут speed для определения скорости бегуна.
# 2. Метод __eq__ для сравнивания имён бегунов.
# 3. Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.

# Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и список
# участников. Также присутствует метод start, который реализует логику бега по предложенной дистанции

# Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:
# I
# setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты всех
# тестов.
# II
# setUp - метод, где создаются 3 объекта:
# 1. Бегун по имени Усэйн, со скоростью 10.
# 2. Бегун по имени Андрей, со скоростью 9.
# 3. Бегун по имени Ник, со скоростью 3.
# III
# tearDownClass - метод, где выводятся all_results по очереди в столбец.

# Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса Tournament
# запускается метод start, который возвращает словарь в переменную all_results. В конце вызывается метод assertTrue, в
# котором сравниваются последний объект из all_results (брать по наибольшему ключу) и предполагаемое имя последнего
# бегуна.

# Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
# 1. Усэйн и Ник
# 2. Андрей и Ник
# 3. Усэйн, Андрей и Ник.
# Как можно понять: Ник всегда должен быть последним.

# Дополнительно (не обязательно, не влияет на зачёт):
# В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка. В результате его работы бегун
# с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
# Попробуйте решить эту проблему и обложить дополнительными тестами.

# Пример результата выполнения тестов:
# Вывод на консоль:
# {1: Усэйн, 2: Ник}
# {1: Андрей, 2: Ник}
# {1: Андрей, 2: Усэйн, 3: Ник}
# Ran 3 tests in 0.001s
# OK

# Примечания:
# Ваш код может отличаться от строгой последовательности описанной в задании. Главное - схожая логика работы тестов и
# наличие всех перечисленных переопределённых методов из класса TestCase.

# Импортировал проверяемы код и unittest
import runner_and_tournament
import unittest


# Arrange-Act-Assert: A Pattern for Writing Good Tests
# https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/

# Создал класс TournamentTest, наследованный от TestCase
class TournamentTest(unittest.TestCase):
    # Создал метод setUpClass, в котором создаётся атрибут класса all_results. Это словарь в который будут сохраняться
    # результаты всех тестов.
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    # Создал setUp - метод, где создаются 3 объекта:
    # 1. Бегун по имени Усэйн, со скоростью 10.
    # 2. Бегун по имени Андрей, со скоростью 9.
    # 3. Бегун по имени Ник, со скоростью 3.
    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner_2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner_3 = runner_and_tournament.Runner('Ник', 3)

    # Создал метод tearDownClass, в котором выводятся all_results по очереди в столбец.
    @classmethod
    def tearDownClass(cls):
        # Форматирование вывода
        for i in cls.all_results.values():
            print({number: str(runner) for number, runner in i.items()})

    # 1. Усэйн и Ник
    def test_run_1(self):
        # Arrange
        tournament_1 = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)

        # Act
        tournament_1_result = tournament_1.start()
        TournamentTest.all_results['result_1'] = tournament_1_result

        # Assert
        self.assertTrue(tournament_1_result.get(max(tournament_1_result)) == self.runner_3)

    # 2. Андрей и Ник
    def test_run_2(self):
        # Arrange
        tournament_2 = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)

        # Act
        tournament_2_result = tournament_2.start()
        TournamentTest.all_results['result_2'] = tournament_2_result

        # Assert
        self.assertTrue(tournament_2_result.get(max(tournament_2_result)) == self.runner_3)

    # 3. Усэйн, Андрей и Ник.
    def test_run_3(self):
        # Arrange
        tournament_3 = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2,
                                                        self.runner_3)

        # Act
        tournament_3_result = tournament_3.start()
        TournamentTest.all_results['result_3'] = tournament_3_result

        # Assert
        self.assertTrue(tournament_3_result.get(max(tournament_3_result)) == self.runner_3)

    # 4. Тест для проверки исправления бага с маленькими дистанциями
    def test_run_4(self):
        # Arrange
        tournament_4 = runner_and_tournament.Tournament(2, self.runner_1, self.runner_2,
                                                        self.runner_3)

        # Act
        tournament_4_result = tournament_4.start()
        TournamentTest.all_results['result_4'] = tournament_4_result

        # Assert
        self.assertTrue(tournament_4_result.get(max(tournament_4_result)) == self.runner_3)


# Запуск тестов
if __name__ == '__main__':
    unittest.main()
