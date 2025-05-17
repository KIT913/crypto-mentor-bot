import telebot
from flask import Flask, request
import threading

API_TOKEN = '7831525545:AAE2ndGlPoZ1vQWHmPW24aKDwCoWrhguP-g'
admin_id = 7928644968

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def welcome(message):
    user = message.from_user
    chat_id = message.chat.id

    # Уведомление админу
    notify_admin = (
        f"🚨 New user launched the bot!\n"
        f"Name: {user.first_name} {user.last_name or ''}\n"
        f"Username: @{user.username}\n"
        f"User ID: {user.id}"
    )
    bot.send_message(admin_id, notify_admin)

    # Сообщение клиенту
    caption = (
        "🖐🏼 Glad to see you on our👉🏻 CHANNEL 👈🏻\n\n"
        "We are the «CRYPTO MENTOR | KIT grp» community\n\n"
        "📊 Our team is based on Futures market analysis.\n"
        "The winning percentage of our Signals is now 97% ✅\n\n"
        "📲 Join now"
    )

    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(
        telebot.types.InlineKeyboardButton("CHANNEL➜📲", url="https://t.me/+V8FKWfygiRY4Nzcx"),
        telebot.types.InlineKeyboardButton("GET FREE SIGNAL✅", url="https://t.me/Kit_futures?text=I%20WANT%20SIGNAL")
    )
    bot.send_message(chat_id, caption, reply_markup=markup)

# Flask + keep alive
@app.route('/')
def index():
    return 'Bot is running!'

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def run_bot():
    bot.infinity_polling()

if name == '__main__':
    threading.Thread(target=run_flask).start()
    run_bot()
