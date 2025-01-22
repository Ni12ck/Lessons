# Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:

# 1. test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у
# этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
# 2. test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у этого
# объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
# 3. test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у объектов
# вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте метод assertNotEqual,
# чтобы убедится в неравенстве результатов.

# Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.

import runner
import unittest


# Создал класс RunnerTest, наследуемый от TestCase из модуля unittest
class RunnerTest(unittest.TestCase):
    # Создал метод test_walk
    def test_walk(self):
        # Создал объект класса Runner
        runner_1 = runner.Runner('Ni12ck')
        # Вызвал метод walk у этого объекта 10 раз
        for i in range(10):
            runner_1.walk()
        # Методом assertEqual сравнил distance этого объекта со значением 50
        self.assertEqual(runner_1.distance, 50)

        # Если поменять значение на 51, то тест не будет пройден, так как ожидаемый результат (51) не будет совпадать с
        # получившимся (50) - AssertionError: 50 != 51
        # self.assertEqual(runner_1.distance, 51)

    # Создал метод test_run
    def test_run(self):
        # Создал объект класса Runner
        runner_2 = runner.Runner('ve_ronyca')
        # Вызвал метод run у этого объекта 10 раз
        for i in range(10):
            runner_2.run()
        # Методом assertEqual сравнил distance этого объекта со значением 100
        self.assertEqual(runner_2.distance, 100)

    # Создал метод test_challenge
    def test_challenge(self):
        # Создал два объекта класса Runner
        runner_3 = runner.Runner('Challenge_1')
        runner_4 = runner.Runner('Challenge_2')
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
