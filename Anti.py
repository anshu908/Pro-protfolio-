import telebot

Token = "ENTER UR BOT TOKEN"

bot = telebot.TeleBot(Token)

@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message, "welcome to my bot if u want any hacking course use /help OWNER OF THIS BOT t.me/ansh_hack  ")


@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message,"""/start-> t.me/ansh_hack  /help ->  """)



@bot.message_handler()
def custom(message):
    try:
        msg = eval(message.text.strip())
    except Exception as e:
        msg = "this can't be evaluated"
        bot.reply_to(message,msg)
     

bot.polling()
