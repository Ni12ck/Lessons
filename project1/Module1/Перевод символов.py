# Экранирование символа с помощью \
print("it's \"alive\""+"\\")
# создаём отображение
mapping = str.maketrans('qwertyuiop[]asdfghjkl;\'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?`~', 'йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,ёЁ')
# преобразуем строку
Translate = input('Введите текст, который надо перевести:')
print('Перевод английских символов на клавиатуре в русские:', Translate.translate(mapping))
