import telebot
import os
from flask import Flask, request

API_TOKEN = "7831525545:AAE2ndGlPoZ1vQWHmPW24aKDwCoWrhguP-g"
admin_id = 7928644968

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton("CHANNEL➡️", url="https://t.me/+lxFWpKJ49J8wN2Vh")
    btn2 = telebot.types.InlineKeyboardButton("GET FREE SIGNAL", url="https://t.me/Kit_futures?text=I%20WANT%20SIGNAL")
    markup.row(btn1, btn2)

    bot.send_message(message.chat.id, 
        "🤚🏻 Glad to see you on our👉🏻 CHANNEL👈🏻\n\n"
        "We are the «CRYPTO MENTOR | KIT grp» community💎\n\n"
        "📊 Our team is based on Futures market analysis.\n"
        "The winning percentage of our Signals is now 97% ✅\n\n"
        "📲 Join now", reply_markup=markup)

    bot.send_message(admin_id, f"👤 New user launched the bot!\n▪️ Name: {message.from_user.first_name}\n▪️ Username: @{message.from_user.username}\n▪️ ID: {message.from_user.id}")

@app.route(f'/{API_TOKEN}', methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return '', 200

@app.route('/')
def index():
    return "Bot is live", 200

if name == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"https://crypto-mentor-bot.onrender.com/{API_TOKEN}")
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
