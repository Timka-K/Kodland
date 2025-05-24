import telebot
import requests
from config import token

bot = telebot.TeleBot(token)
WEATHER_TOKEN = 'YOUR OPEN WEATHER API KEY'


def get_weather():
    city = 'Москва'# yuor city name
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}&units=metric&lang=ru'
    resp = requests.get(url).json()
    if resp.get('weather') and resp.get('main'):
        description = resp['weather'][0]['description'].capitalize()
        temp = resp['main']['temp']
        humidity = resp['main']['humidity']
        message = (
            f"🏞Погода в городе {city}:\n"
            f"{description}\n"
            f"Температура🌡: {temp}°C\n"
            f"Влажность💧: {humidity}%"
        )
    else:
        message = "Не получилось найти данные о погоде."
    return message

@bot.message_handler(commands=['weather'])
def send_weather(message):
    weather_msg = get_weather()
    bot.send_message(message.chat.id, weather_msg)

bot.polling()
