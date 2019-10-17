import telebot
import pyowm

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc')
bot = telebot.TeleBot("957770386:AAG9AH13DUZB7CnYPqkSX9epfrFDK779lao")

@bot.message_handler(content_types = ['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    answer = 'There is ' + w.get_detailed_status() + ' in ' + message.text + '\n'
    answer += 'The temperature is around ' + str(temp) + ' degrees' + '\n\n'
    if temp <= 0:
        answer += 'It\'s too cold, bruh. U\'d better dress warmly.'
    elif temp < 10:
        answer += 'It\'s a lil bit cold, bruh. Dress moderately warm clothes.'
    elif temp < 20:
        answer += 'It\'s not so cold, bruh. Dress smth like sweater and usual jeans.'
    else:
        answer += 'It\'s so warm, dude. Feel free to wear what u want.'
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)