import telebot 
from telebot import types


bot = telebot.TeleBot('7530076268:AAGtH4QqmTEWUn_KS6hos3U7xMovZUjU1Xo')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Русский', callback_data='Rus')
    btn2 = types.InlineKeyboardButton(text='O\'zbek', callback_data='Uzb')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text='Выбирите язык\nTil tanlang', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def call_handler(call):
    if call.data == 'Rus':
        bot.send_message(call.message.chat.id, text='Бот находить временно на разработки')
    elif call.data == 'Uzb':
        bot.send_message(call.message.chat.id, text='Bot vaqtincha ishlabchiqarish jarayonida ')

if __name__ == '__main__':
    bot.polling(none_stop=True)