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

if __name__ == '__main__':
    main(True, 'DEBUG')
