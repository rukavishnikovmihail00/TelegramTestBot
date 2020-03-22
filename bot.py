import telebot
import random
from telebot import types
token = '1109775017:AAFwU9OOhl5bVsMgRUa6zB82i2gy5VJ3NW0'



bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Случайное число")
    item2 = types.KeyboardButton("Как дела?")
    markup.add(item1,item2)
    bot.send_message(message.chat.id, "Привет! Я - бот, созданный, чтобы ничего не делать.", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def obrabotchik(message):
    if message.chat.type == 'private':
        if message.text == 'Случайное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == 'Как дела?':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            markup.add(item1,item2)

            bot.send_message(message.chat.id, 'Отлично! А у тебя?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю, что ответить')

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отлично')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Ой-ой')

    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)