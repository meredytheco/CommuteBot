# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '132942964:AAE_QjDxiOz36LzBsOhcj80sZu-DFml-0xo'
WEATHER_API_KEY='f08b39df8a0912e0'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(msg):
    bot.reply_to(msg, """\
Hi, I'm Boston Commute Bot! Text me for a report on what to reasonably expect on your commute\
""")
@bot.message_handler(commands=['go','weather'])
def handle_message(msg):
	bot.reply_to(msg, text="It's probably raining.")
@bot.message_handler(commands=['station'])
def handle_message(msg):
	bot.reply_to(msg, text="This feature of mine is still under development, but I'll do my best to help. Which station on the Red or Green Line do you want to know about?")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
#@bot.message_handler(func=lambda message: True)
#def echo_message(message):
 #   bot.reply_to(message, message.text)

bot.polling()