import telebot
from flask import Flask, request
import os

API_TOKEN = '7831525545:AAE2ndGlPoZ1vQWHmPW24aKDwCoWrhguP-g'
bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    text = (
        "🖐 Glad to see you on our👉🏻 *CHANNEL* 👈🏻\n\n"
        "We are the «*CRYPTO MENTOR | KIT grp*» community💎\n\n"
        "📊 *Our team is based on Futures market analysis.*\n"
        "*The winning percentage of our Signals is now 97%* ✅\n\n"
        "📲 [Join now](https://t.me/+lxFWpKJ49J8wN2Vh)"
    )

    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(
        telebot.types.InlineKeyboardButton("CHANNEL➜📲", url="https://t.me/+lxFWpKJ49J8wN2Vh"),
        telebot.types.InlineKeyboardButton("GET FREE SIGNAL", url="https://t.me/Kit_futures?text=I%20WANT%20SIGNAL")
    )

    bot.send_message(chat_id, text, parse_mode="Markdown", reply_markup=markup)

@server.route(f"/{API_TOKEN}", methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return {"ok": True}

@server.route("/")
def index():
    return "Bot is live!"

bot.remove_webhook()
bot.set_webhook(url=f"https://crypto-mentor-bot.onrender.com/{API_TOKEN}")

if name == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
