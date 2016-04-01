import sys
import time
import telebot
import requests
import unirest

TOKEN = '132942964:AAE_QjDxiOz36LzBsOhcj80sZu-DFml-0xo'
BASE_URL = "https://api.telegram/org/bot/"+TOKEN
POLLING_URL = BASE_URL + "getUPdates?offset=:offset&timeout=60"
SEND_MESSAGE_URL = BASE_URL + "sendMessage"

WEATHER_API_KEY='f08b39df8a0912e0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def send_welcome(msg):
	bot.reply_to(msg, "Welcome! Text me for a report on what to reasonably expect on your commute")
@bot.message_handler(commands=['go','weather','station'])
def handle_message(msg):
	bot.reply_to(msg.message_id, text="i got nothing for you")
@bot.message_handler(commands='station')
def handle_message(msg):
	bot.reply_to(msg, "This feature of mine is still under development")

@bot.message_handler(func=lambda m:True)
def echo_all(msg):
	print(msg.text)
bot.polling()