# 1.Фикстура – конкретный тест, т.е. некоторый элемент, который позволяет произвести подготовку для выполнения тестов,
# так же саму отработку теста и мероприятие по его завершению.
# 2.«TestCase» - набор тестов, который мы имеем в виду. Мы ее воспринимаем как элементарную единицу тестирования, в
# рамках которой проходят различные фикстуры.
# 3.«Test Suite» - набор тестов, тест-кейсов, который позволяет выполнять системы и их отдельно проверять. Количество
# таких тест-кейсов не ограничено.
# 4.«Test Runner» - компонент, который отвечает за запуск проверки тестирования и того, как со всем этим
# взаимодействовать.

# Кроме вышеперечисленного доступно еще 3 типа вещей того, что можно сделать с нашим тест-кейсом.
# 1.Методы, запускаемые при запуске теста
# 2.Методы, запускаемые после тестов
# 3.Методы, которые запускаются при написании, проверке теста
# 4. Так же есть метод, который позволяет собирать информацию.

import calc
import unittest


class CalcTest(unittest.TestCase):
    # Метод «def setUp»
    # Это метод, который производится перед каждым тестированием
    # При каждой отработке теста выводится «setUp». ВАЖНО! Перед «Test_abb», «test_sub» производится функция «setUp»,
    # в ней можно производить какие-то действия заранее.
    def setUp(self):
        print('setup')

    # Функция «setUpClass»
    # Для нее нужно указать декоратор через @, она называется «setUpClass». Напишем «MegaSetup». «MegaSetup» происходит
    # в самом начале и 1 раз.
    @classmethod
    def setUpClass(cls):
        print('MegaSetUp')

    # И есть подобные методы, но которые производятся после выполнения тестов
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_add(self):
        # assert - проверить
        """
        Test for add function in calc
        :return:
        """
        self.assertEqual(calc.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(calc.sub(2, 1), 1)

    def test_mul(self):
        self.assertEqual(calc.mul(2, 2), 4)

    def test_div(self):
        self.assertEqual(calc.div(4, 2), 2)

    # «assertEqual» - достаточно стандартный вариант, который используется для сравнения
    # Есть большое количество методов (assert)
    # - «assertTrue» позволяет проверить равна ли передаваемая переменная. Можем передать некую логическую переменную
    # - «assertFalse» проверяет не равно ли значение «False».
    # - «assertIs» позволяет проверять через оператор «Is» является ли «a, b» «a Is b».
    # - «assertIsNone» проверяет не равна ли переменная пустому значению. Если она пустая, то вернется «True», если не
    # пустая, то «notNone» (False).
    # - «assertIn» - проверка наличия, подходит для строк. Проверяем есть ли строка «a» в строке «b»
    # - «assertRaises» позволяет проверять была ли вызвана какая-либо ошибка, например, деление на 0
    # - «assertWarnings» (ворнинги) можно их получать и проверять не появились ли они. Для них есть доп. функция через
    # регулярные выражения.
    # - «assertAlmostEquals» - функция, которая позволяет сравнить 2 числа с точностью до 7 знака после запятой. Это
    # нужно для сравнения вещественных чисел. Виду специфики хранения вещественных чисел, они могут отличаться,
    # например, на 25 знаке, в зависимости от того, как они хранятся. (Есть так же «assertAlmostNotEquals»)
    # - «assertGreater», «assertNotGreater», «assertGreaterEqual», «assertLess», «assertLessEqual», т.е. больше, больше
    # либо равно, меньше, меньше либо равно.

if __name__ == '__main__':
    unittest.main()
