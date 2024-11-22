import telebot
import os
import pywttr
from datetime import datetime
import pyjokes

language = pywttr.Language.RU
bot = telebot.TeleBot(os.environ.get('TelegramToken'))
current_month = datetime.now().month


# Работа с функцией get_weather_in для конкретного города
@bot.message_handler(commands=['weather'])
def get_weather(message):
    get_weather_in(message, 'Иваново')


@bot.message_handler(commands=['Ni12ck'])
def cr_ni12ck(message):
    bot.send_message(message.from_user.id, 'Здравствуй создатель! Моя миссия выводить погоду?😢 О нет😱')


@bot.message_handler(commands=['Renton'])
def renton(message):
    bot.send_message(message.from_user.id, 'https://www.japandict.com/')

@bot.message_handler(commands=['WorkingOwl'])
def workingowl(message):
    bot.send_message(message.from_user.id, 'Го в форточку? \n https://i.gifer.com/WxTz.gif')


@bot.message_handler(commands=['help', 'start'])
def get_help(message):
    bot.send_message(message.from_user.id, 'Введите название города, чтобы получить прогноз погоды на завтра \n'
                                           'Хотите анекдот? - /joke \n'
                                           'Японский словарь - /Renton \n'
                                           'Список покупок - /purchases \n'
                                           'Добавление товара - /add "сообщение" \n'
                                           'Fortnite - /WorkingOwl')


@bot.message_handler(commands=['joke'])
def joke_bot(message):
    bot.send_message(message.from_user.id, pyjokes.get_joke('ru'))


# Создаёт файл "purchases.txt" для чтения, если его нет. Отправляет текст из файла пользователю.
@bot.message_handler(commands=['purchases'])
def get_purchases(message):
    # encoding="utf-8" - позволяет работать с кириллицей, 'r' - работает как read
    with open('purchases.txt', 'r', encoding='utf-8') as file:
        purchases = file.read()
        bot.send_message(message.from_user.id, purchases)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если пользователь пишет "/add сообщение", то это сообщение записывается в "purchases.txt"
    if message.text.startswith('/add'):
        # encoding="utf-8" - позволяет работать с кириллицей, "a+" - работает как append
        with open('purchases.txt', 'a+', encoding='utf-8') as file:
            # Запись сообщения в "purchases.txt", при этом '/add 'заменяется на пробел
            file.write(message.text.replace('/add ', '') + '\n')
    else:
        # Отлов ошибок - название города
        try:
            get_weather_in(message, message.text)
        except:
            bot.send_message(message.from_user.id, "Вы ввели неверное название города, попробуйте снова")


# Функция принимает сообщение от пользователя с названием города и присылает прогноз пользователю
def get_weather_in(message, location):
    weather = pywttr.get_weather(location, language)  # language = pywttr.Language.RU

    # current_month = datetime.now().month
    emoji = ''
    if 6 <= current_month <= 8:
        emoji = '☀️'
    elif 9 <= current_month <= 11:
        emoji = '🍂'
    elif 1 <= current_month <= 2 or current_month == 12:
        emoji = '❄️'
    elif 3 <= current_month <= 5:
        emoji = '🌸'

    bot.send_message(message.from_user.id,
                     f'Текущая температура в городе {location}: {weather.current_condition[0].temp_c}С \n'
                     f'Погода в городе {location} завтра ({emoji} '
                     # Сначала идёт парсинг строки str p, а потом форматирование str f 
                     f'{datetime.strptime(weather.weather[1].date, '%Y-%m-%d').strftime('%d.%m.%Y')} {emoji}) \n'
                     f'Средняя температура: {weather.weather[1].avgtemp_c}С \n'
                     f'Минимальная температура: {weather.weather[1].mintemp_c}С \n'
                     f'Максимальная температура: {weather.weather[1].maxtemp_c}С')


bot.infinity_polling()
