from random import choice
Hangman = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |    |
     | 
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |   
     |     
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ----------
    """
)
max_wrong = len(Hangman) - 1
# print(type(len))
# len() — встроенный метод Python для нахождения длины списка.
# На вход метод принимает один параметр: сам список.
# В качестве результата len() возвращает целочисленное значение — длину списка.
# Также этот метод работает и с другими итеративными объектами, например со строками
# Country_list = ["The United States of America", "The Russian Federation", "France", "Germany"]
# count = len(Country_list)
# print("There are", count, "countries")
# Вывод:
# There are 4 countries
Word_list = ('москва', 'казань', 'петербург', 'иваново', 'анапа', 'сочи') # Слова для угадывания
Word = choice(Word_list)  # Слово, которое нужно угадать
length = "_" * len(Word)  # Одна черточка для каждой буквы в слове, которое нужно угадать
wrong = 0  # Количество неверных предположений, сделанных игроком
used = []  # Буквы уже угаданы
# Цикл, который будет работать до тех пор,
# пока число максимальных ошибок не превысит количество имеющихся попыток и пока слово не будет угадано:
while wrong < max_wrong and length != Word:
    print(Hangman[wrong])  # Вывод висельника по индексу
    print("\nВы использовали следующие буквы:\n", used)
    print("\nНа данный момент слово выглядит так:\n", length)

    assumption = input("\n\nВведите свое предположение: ")  # Пользователь вводит предполагаемую букву

    while assumption in used:
        print("Вы уже вводили букву", assumption)  # Если буква уже вводилась ранее, то выводим соответствующее сообщение
        assumption = input("Введите свое предположение: ")  # Пользователь вводит предполагаемую букву

    used.append(assumption)  # В список использованных букв добавляется введённая буква
# append() принимает один аргумент item и добавляет его в конец list.
# Тип параметра может быть любым: числа, строки, словари и так далее. Метод возвращает объект None — то есть ничего.
    if assumption in Word:  # Если введённая буква есть в загаданном слове, то выводим соответствующее сообщение
        print("\nДа!", assumption, "есть в слове!")
        new = ""
        for i in range(len(Word)):  # В цикле добавляем найденную букву в нужное место
            if assumption == Word[i]:
                new += assumption
            else:
                new += length[i]
        length = new

    else:
        print("\nИзвините, буквы \"" + assumption + "\" нет в слове.")  # Если буквы нет, то выводим соответствующее сообщение
        wrong += 1
if wrong == max_wrong:  # Если игрок превысил кол-во ошибок, то его повесили
    print(Hangman[wrong])
    print("\nВы проиграли :(")
else:  # Если кол-во ошибок не превышено, то игрок выиграл
    print("\nВы угадали слово!")
print("\nЗагаданное слово было \"" + Word + '\"')