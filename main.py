import telebot
import json

from config import TELEGRAM_TOKEN


bot = telebot.TeleBot(TELEGRAM_TOKEN)

with open('cities.json', encoding='utf-8') as f:
    cities = json.load(f)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    text = (
        f'Привет!Этот бот выдает координаты введенного вами города.Введите название города'
    )
    bot.reply_to(message, text)


@bot.message_handler()
def get_coordinates(message):
    city_name = message.text

    if city_name in cities:
        coordinates = cities[city_name]
        bot.send_message(message.chat.id, f'Координаты города {city_name}: {coordinates}')
    else:
        bot.send_message(
            message.chat.id, 'Отсутствуют данные о координатах введенного вами города.')


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
