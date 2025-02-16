import discord
import os
from discord.ext import commands
import random

client = discord.Client()
token = 'YOUR TOKEN'

def load_cities():
    with open('cities.txt', 'r', encoding='utf-8') as f:
        cities = f.readlines()
        cleaned_cities = []
        for city in cities:
            city = city.lower().replace('Оспаривается', '').replace('\n', '')
            if city != '':
                cleaned_cities.append(city)
    return cleaned_cities

cities = load_cities()

used_words = []

@client.event
async def on_message(message):
    global used_words
    if message.author == client.user:
        return
    if message.content == '$start':
        used_words = []
        await message.channel.send("Игра запущена, пиши название города")
        return
    word = message.content.lower()
    if word in used_words:
        await message.channel.send('Такое слово уже было использовано, ты проиграл!')
        return
    if word in cities:
        used_words.append(word)
        i = 1
        while word[-i] in 'ыйьъ':
            i += 1
        for city in cities:
            if city not in used_words and city[0] == word[-i]:
                await message.channel.send(city)
                used_words.append(city)
                return
        await message.channel.send('Не могу ничего придумать. Ты победил')
    else:
        await message.channel.send('Такого города нет, ты проиграл')
        
client.run(token)
