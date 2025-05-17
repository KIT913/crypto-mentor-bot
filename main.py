import telebot
from telebot import types

bot = telebot.TeleBot("7831525545:AAE2ndGlPoZ1vQWHmPW24aKDwCoWrhguP-g")
admin_id = 7928644968

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("CHANNEL➡️", url="https://t.me/+lxFWpKJ49J8wN2Vh")
    btn2 = types.InlineKeyboardButton("GET FREE SIGNAL", url="https://t.me/Kit_futures?text=I%20WANT%20SIGNAL")
    markup.row(btn1, btn2)

    bot.send_message(message.chat.id, 
        "🤚🏻 Glad to see you on our👉🏻 CHANNEL👈🏻\n\n"
        "We are the «CRYPTO MENTOR | KIT grp» community💎\n\n"
        "📊 Our team is based on Futures market analysis.\n"
        "The winning percentage of our Signals is now 97% ✅\n\n"
        "📲 Join now", reply_markup=markup)

    bot.send_message(admin_id, f"👤 New user launched the bot!\n▪️ Name: {message.from_user.first_name}\n▪️ Username: @{message.from_user.username}\n▪️ ID: {message.from_user.id}")

bot.polling(none_stop=True)
