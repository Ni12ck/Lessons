# Импортировал проверяемы код и unittest
import runner_and_tournament
import unittest

# Создал класс TournamentTest, наследованный от TestCase
class TournamentTest(unittest.TestCase):
    # Добавил атрибут is_frozen = True
    is_frozen = True
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

    # Написал соответствующий декоратор к каждому методу (кроме @classmethod), который при значении is_frozen = False
    # будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение 'Тесты в этом кейсе заморожены'.
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    # 1. Усэйн и Ник
    def test_run_1(self):
        # Arrange
        tournament_1 = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)

        # Act
        tournament_1_result = tournament_1.start()
        TournamentTest.all_results['result_1'] = tournament_1_result

        # Assert
        self.assertTrue(tournament_1_result.get(max(tournament_1_result)) == self.runner_3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    # 2. Андрей и Ник
    def test_run_2(self):
        # Arrange
        tournament_2 = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)

        # Act
        tournament_2_result = tournament_2.start()
        TournamentTest.all_results['result_2'] = tournament_2_result

        # Assert
        self.assertTrue(tournament_2_result.get(max(tournament_2_result)) == self.runner_3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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
