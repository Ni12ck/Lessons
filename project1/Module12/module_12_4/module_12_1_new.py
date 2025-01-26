import runner_and_tournament
import unittest


# Создал класс RunnerTest, наследуемый от TestCase из модуля unittest
class RunnerTest(unittest.TestCase):
    # Добавил атрибут is_frozen = False
    is_frozen = False

    # Написал соответствующий декоратор к каждому методу (кроме @classmethod), который при значении is_frozen = False
    # будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение 'Тесты в этом кейсе заморожены'.
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    # Создал метод test_walk
    def test_walk(self):
        # Создал объект класса Runner
        runner_1 = runner_and_tournament.Runner('Ni12ck')
        # Вызвал метод walk у этого объекта 10 раз
        for i in range(10):
            runner_1.walk()
        # Методом assertEqual сравнил distance этого объекта со значением 50
        self.assertEqual(runner_1.distance, 50)

        # Если поменять значение на 51, то тест не будет пройден, так как ожидаемый результат (51) не будет совпадать с
        # получившимся (50) - AssertionError: 50 != 51
        # self.assertEqual(runner_1.distance, 51)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    # Создал метод test_run
    def test_run(self):
        # Создал объект класса Runner
        runner_2 = runner_and_tournament.Runner('ve_ronyca')
        # Вызвал метод run у этого объекта 10 раз
        for i in range(10):
            runner_2.run()
        # Методом assertEqual сравнил distance этого объекта со значением 100
        self.assertEqual(runner_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    # Создал метод test_challenge
    def test_challenge(self):
        # Создал два объекта класса Runner
        runner_3 = runner_and_tournament.Runner('Challenge_1')
        runner_4 = runner_and_tournament.Runner('Challenge_2')
        # Вызвал метод walk у объекта runner_3 10 раз
        for i in range(10):
            runner_3.walk()
        # Вызвал метод run у объекта runner_4 10 раз
        for i in range(10):
            runner_4.run()
        # Методом assertNotEqual проверяю неравенство результатов
        self.assertNotEqual(runner_3.distance, runner_4.distance)


# Запуск тестов
if __name__ == '__main__':
    unittest.main()
