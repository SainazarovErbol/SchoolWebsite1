import telebot

bot = telebot.TeleBot('7081450971:AAHqjBDuYxeKVqHeAwAuRdTcQZTD8H4LAhA')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')


@bot.message_handlers()
def welcom(message):
    if message.text.lower() == 'инфа':
        bot.send_message(message, f'Привет {message.from_user.first_name},')


bot.polling(none_stop=True)
