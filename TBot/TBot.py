import telebot
import os
import pywttr
from datetime import datetime
import pyjokes

language = pywttr.Language.RU
bot = telebot.TeleBot(os.environ.get('TelegramToken'))
current_month = datetime.now().month


@bot.message_handler(commands=['weather'])
def get_weather(message):
    get_weather_in(message, 'Иваново')


@bot.message_handler(commands=['Ni12ck'])
def cr_ni12ck(message):
    bot.send_message(message.from_user.id, 'Здравствуй создатель! Моя миссия выводить погоду?😢 О нет😱')


@bot.message_handler(commands=['help', 'start'])
def get_help(message):
    bot.send_message(message.from_user.id, 'Введите название города, чтобы получить прогноз погоды на завтра \n'
                                           'Хотите анекдот? - /joke ')


@bot.message_handler(commands=['joke'])
def joke_bot(message):
    bot.send_message(message.from_user.id, pyjokes.get_joke('ru'))


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    try:
        get_weather_in(message, message.text)
    except:
        bot.send_message(message.from_user.id, "Неверное название города")


def get_weather_in(message, location):
    weather = pywttr.get_weather(location, language)

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
                     f'Погода в городе {location} завтра ({emoji} {weather.weather[1].date} {emoji}) \n'
                     f'Средняя температура: {weather.weather[1].avgtemp_c}С \n'
                     f'Минимальная температура: {weather.weather[1].mintemp_c}С \n'
                     f'Максимальная температура: {weather.weather[1].maxtemp_c}С')


bot.infinity_polling()
