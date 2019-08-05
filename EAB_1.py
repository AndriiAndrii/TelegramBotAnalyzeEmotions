
import telebot

API_TOKEN = '****************************'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EAB.\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    #bot.reply_to(message, 'recorded')
    f = open('text.txt', 'a')
    f.write('text: ' + str(message.text)+ ' chat_id: ' + str(message.chat.id) + ' date: ' + str(message.date)  #'user_id ' + str(message.from.id)
            + '\n')
    f.close()


bot.polling()
