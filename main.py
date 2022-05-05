import telebot
from telebot import types
import os
from random import choice, shuffle
from country_dict import country_dict, dict_country

bot = telebot.TeleBot('5321028088:AAEXqF0H3Lh_GBiPdLdR8ltA_91D1TzGcbk')
questions = ['Какой страны этот флаг?', 'Что же это за страна?', 'Какая страна?', 'Флаг какой страны ты видишь?',
             'А а это что за страна?']
RIGHT = 0
WRONG = 0


@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.username != None:
        mess = f"""Привет, <b>{message.from_user.username}</b>!
Ты хочешь начать угадывать?
Если да, нажми "начать". 
Для дополнотельной информациии нажми <b>/help</b>"""
    else:
        mess = f"""Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>!
Ты хочешь начать угадывать?
Если да, нажми "начать". 
Для дополнотельной информациии нажми <b>/help</b>"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    start_game = types.KeyboardButton('начать')
    help = types.KeyboardButton('/help')
    markup.add(start_game, help)
    bot.send_message(message.chat.id, mess,
                     reply_markup=markup, parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    if message.from_user.username != None:
        mess = f"""Привет, <b>{message.from_user.username}</b>!
Этот бот поможет тебе проверить знания флагов стран или просто развлечься.
Вот список доступных тебе команд:
<b>/start</b> - начать работу с ботом"""
    else:
        mess = f"""Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>!
Этот бот поможет тебе проверить знания флагов стран или просто развлечься.
Вот список доступных тебе команд:
<b>/start</b> - начать работу с ботом"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    start = types.KeyboardButton('/start')
    markup.add(start)
    bot.send_message(message.chat.id, mess,
                     reply_markup=markup, parse_mode='html')


@bot.message_handler(commands=['stop'])
def stop(message):
    global RIGHT, WRONG
    RIGHT = 0
    WRONG = 0
    mess = f"""Ты хочешь начать угадывать снова?
Если да, нажми "начать". 
Для дополнотельной информациии нажми <b>/help</b>"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    start_game = types.KeyboardButton('начать')
    help = types.KeyboardButton('/help')
    markup.add(start_game, help)
    bot.send_message(message.chat.id, mess,
                     reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    global RIGHT, WRONG
    if message.text.lower() == 'начать':
        main_game(message)
    elif message.text == country_dict[pic.upper()]:
        RIGHT += 1
        bot.send_message(message.chat.id, f"""<b>Правильно!</b> 
Правильных: {RIGHT}
Неправильных: {WRONG}""", parse_mode='html')
        main_game(message)
    elif message.text != country_dict[pic.upper()] and message.text in rand:
        WRONG += 1
        bot.send_message(message.chat.id, f"""<b>Неправильно(</b>
Правильный ответ: <strong>{country_dict[pic.upper()]}</strong>
Правильных: {RIGHT}
Неправильных: {WRONG}""", parse_mode='html')
        main_game(message)
    elif message.text == 'здесь если ты не мент то ты мусор':
        music = open('egg.mp3', 'rb')
        bot.send_audio(message.chat.id, music)
    else:
        bot.send_message(message.chat.id, """Я тебя не понимаю. Вот список доступных тебе команд: 
<b>/start</b> - начать работу с ботом.
<b>/help</b> - узнать дополнительную информацию.""", parse_mode='html')


def pic_list():
    files = os.listdir('data')
    spisok = []
    for i in files:
        spisok.append(i[:-4])
    return spisok


def random_country(right):
    random_country = []
    val = list(country_dict.values())
    random_country.append(country_dict[right.upper()])
    val.remove(country_dict[right.upper()])
    for i in range(3):
        rand = choice(val)
        random_country.append(rand)
        val.remove(rand)
    shuffle(random_country)
    return random_country


@bot.message_handler(content_types=['text'])
def main_game(message):
    global pic
    global rand
    pic = choice(pic_list())
    photo = open(f'data/{pic}.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    mess = choice(questions)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    rand = random_country(pic)
    country1 = types.KeyboardButton(rand[0])
    country2 = types.KeyboardButton(rand[1])
    country3 = types.KeyboardButton(rand[2])
    country4 = types.KeyboardButton(rand[3])
    stop = types.KeyboardButton('/stop')
    markup.add(country1, country2, country3, country4, stop)
    bot.send_message(message.chat.id, mess,
                     reply_markup=markup, parse_mode='html')
    return pic, rand


bot.polling(none_stop=True)
