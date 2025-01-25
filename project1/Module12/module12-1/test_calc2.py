import calc
import unittest
import random


class CalcTest(unittest.TestCase):
    def test_add(self):
        # assert - проверить
        """
        Test for add function in calc
        :return:
        """
        self.assertEqual(calc.add(1, 2), 3)

    # Можно пропустить тест, указав причину пропуска
    @unittest.skip('Пока не нужен')
    def test_sub(self):
        self.assertEqual(calc.sub(2, 1), 1)

    # Пропуск по условию, например не пройден основной тест
    @unittest.skipIf(True, 'Тест не прошёл')
    def test_mul(self):
        self.assertEqual(calc.mul(2, 2), 4)

    def test_div(self):
        self.assertEqual(calc.div(4, 2), 2)

if __name__ == '__main__':
    unittest.main()
