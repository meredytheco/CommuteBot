import sys
import time
import pprint
import telegram
import telebot
import requests

TOKEN = '132942964:AAE_QjDxiOz36LzBsOhcj80sZu-DFml-0xo'
WEATHER_API_KEY='f08b39df8a0912e0'
bot = telegram.Bot(TOKEN)
#bot.notifyOnMessage(handle)
def get_weather_report():
    r = requests.get("http://api.wunderground.com/api/"+WEATHER_API_KEY+"/conditions/q/MA/Brookline.json")
    print r.text
    #parse json for temp_f and temperature feels-like (wind mph, precip info if user asks for full weather report)
    #send message like "It's 50 degrees and raining (precip_1hr > 0.00) in Boston. It feels like 40 degrees. Wind is 5mph" 
def weather_message():
    print 'Current conditions in Boston: '
    #if user sends msg 'go' or 'weather' to bot
    #get values from get_weather_report
    #formatting

def handle(msg):
    chat_id = msg['chat']['id']    
    command = msg['text']
    print 'Receieved your command: %s' %command
    if command == '/go':
        #send weather report + T info
        bot.sendMessage(chat_id, weather_message())
    elif command == '/weather':
        bot.sendMessage(chat_id, 'feature not supported yet')
    elif command == '/Station':
        bot.sendMessage(chat_id, 'which station?')
         #then, get "'T stop name'": send realtime T update without weather report
    elif command == '/help':
        bot.sendMessage == (chat_id, 'text /go, /weather, or /station')

updates = bot.getUpdates()
print [u.message.text for u in updates]
#bot gets chat_id and message text from latest user/s
chat_id = bot.getUpdates()[-1].message.chat_id
#if message id is "go": send weather and T info
#if message id is "weather": send more detailed weather report

bot.sendMessage(chat_id=chat_id, text="...nothin")
print bot.getMe()
bot.notifyOnMessage(handle)
bot.notifyOnMessage(run_forever = True)
