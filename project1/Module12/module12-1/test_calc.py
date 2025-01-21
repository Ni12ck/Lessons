import calc


def test_add():
    if calc.add(1, 3) == 4:
        print('Тест на сложение пройден')
    else:
        print('Тест на сложение не пройден!')


def test_sub():
    if calc.sub(4, 3) == 1:
        print('Тест на вычитание пройден')
    else:
        print('Тест на вычитание не пройден!')


def test_mul():
    if calc.mul(2, 2) == 4:
        print('Тест на умножение пройден')
    else:
        print('Тест на умножение не пройден!')


def test_div():
    if calc.div(12, 3) == 4:
        print('Тест на деление пройден')
    else:
        print('Тест на деление не пройден!')


test_add()
test_sub()
test_mul()
test_div()
