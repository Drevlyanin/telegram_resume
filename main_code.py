import telebot

bot = telebot.TeleBot('your_token_here')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твоё резюме. Как я могу тебе помочь?")

bot.polling()

