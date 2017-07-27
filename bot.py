# -*- coding: utf-8 -*-
import telebot
import config
import jagopars
import time

bot = telebot.TeleBot(config.token)
@bot.message_handler(commands = ['info'])
def info_sender(mess):
    bot.send_message(mess.chat.id, "I'm Jarvis, your personal assistant.")

@bot.message_handler(commands = ['jago'])
def jago_sender_comand(mess):
    jago_post = jagopars.get_post()
    bot.send_message(mess.chat.id, jago_post)

@bot.message_handler(commands = ['start'])
def jago_post_check(mess):
    bot.send_message(mess.chat.id, 'Start searching')
    jago_post = jagopars.get_post()
    while True:
        if jago_post != jagopars.get_post():
            bot.send_message(mess.chat.id, jago_post)
        time.sleep(100)
        bot.send_message(mess.chat.id, 'Still searching')

if __name__ == '__main__':
    bot.polling(none_stop=True)   
