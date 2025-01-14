# Рекурсия — это такой способ определения функции или описание функции, когда эта самая функция вызывает саму себя.
# Например, создам функцию, которая будет находить сумму чисел с помощью рекурсии
def summa(value):
    # Работа функции будет останавливаться, когда value будет равен 0
    if value == 0:
        return 0
    else:
        # Либо работа функции остановится в том случае, когда переберутся все значения до 0
        return value + summa(value - 1)


print('Сумма всех чисел до заданного значения:', summa(7))
print()

# Чтобы понять, как это работает, давайте немного поговорим с вами про стек(stack). Что такое стек?
# Стеком называется способ организации данных в памяти компьютера. Этот способ работает по принципу последним пришел,
# первым вышел. Возможно, где-то уже на форумах видели аббревиатуру “LIFO”(Last in first out) — это значит, что
# последний элемент, добавленный в стек, будет взят из него первым. Добавлять новые элементы и удалять существующие
# мы можем только с одного конца, который называется вершиной

# Создам пустой список
# Показ работы со стаками
stack = []
stack.append(1)
print('Добавили элемент в список', stack)
stack.append(2)
print('Добавили элемент в список', stack)
stack.append(3)
print('Добавили элемент в список', stack)
print('Полный список',stack)
stack.pop()
print('Убрали элемент из списка', stack)
stack.pop()
print('Убрали элемент из списка', stack)
stack.pop()
print('Убрали элемент из списка', stack)