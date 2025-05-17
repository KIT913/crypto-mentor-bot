import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '7831525545:AAE2ndGlPoZ1vQWHmPW24aKDwCoWrhguP-g'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id

    # Кнопки
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("CHANNEL➡️", url="https://t.me/+V8FKWfygiRY4Nzcx"),
        InlineKeyboardButton("GET FREE SIGNAL...", url="https://t.me/Kit_futures?text=I%20WANT%20SIGNAL")
    )

    # Текст
    text = (
        "🤚🏼 Glad to see you on our👉🏼 <b>CHANNEL</b> 👈🏼\n\n"
        "We are the «<b>CRYPTO MENTOR | KIT grp</b>» community💎\n\n"
        "📊 Our team is based on Futures market analysis.\n"
        "<b>The winning percentage of our Signals is now 97%</b> ✅\n\n"
        "📲 <b>Join now</b>"
    )

    bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=markup)

if name == "__main__":
    bot.polling()
