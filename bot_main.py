import logging
import telebot
from variables import *

bot = telebot.TeleBot(TOKEN)


def main(use_logging, level_name):
    if use_logging:
        telebot.logger.setLevel(logging.getLevelName(level_name))
    bot.polling(none_stop=True, interval=.5)


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.from_user.id, start_mess)


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.from_user.id, help_mess)


@bot.message_handler(commands=['task'])
def task(message):
    pass


@bot.message_handler(commands=['sub_task'])
def sub_task(message):
    pass


@bot.message_handler(commands=['remainder'])
def remainder(message):
    pass


@bot.message_handler(commands=['list'])
def list_tasks(message):
    pass


@bot.message_handler(commands=['list_today'])
def list_today(message):
    pass


if __name__ == '__main__':
    main(True, 'DEBUG')
