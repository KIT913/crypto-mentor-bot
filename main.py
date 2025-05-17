import telebot
from telebot import types

# Твой токен бота
TOKEN = '7831525545:AAE2ndGlPoZ1vQWHmPW24aKDwCoWrhguP-g'
bot = telebot.TeleBot(TOKEN)

# Твой Telegram ID
admin_id = 7928644968

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Кнопки под сообщением
    markup = types.InlineKeyboardMarkup(row_width=2)
    channel_button = types.InlineKeyboardButton("CHANNEL📲", url="https://t.me/+V8FKWfygiRY4Nzcx")
    signal_button = types.InlineKeyboardButton("GET FREE SIGNAL...", url="https://t.me/Kit_futures?text=I%20WANT%20SIGNAL")
    markup.add(channel_button, signal_button)

    # Текст с кликабельными ссылками (Markdown)
    welcome_text = (
        "👋🏻 Glad to see you on our👉🏻 [CHANNEL](https://t.me/+V8FKWfygiRY4Nzcx) 👈🏻\n\n"
        "We are the «[CRYPTO MENTOR | KIT grp](https://t.me/+V8FKWfygiRY4Nzcx)» community💎\n\n"
        "📊 Our team is based on Futures market analysis.\n"
        "The winning percentage of our Signals is now 97% ✅\n\n"
        "📲 [Join now](https://t.me/+V8FKWfygiRY4Nzcx)"
    )

    # Отправка сообщения клиенту
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=markup)

    # Уведомление тебе в личку
    bot.send_message(admin_id, f"👤 New user launched the bot!\n▪️ Name: {message.from_user.first_name}\n▪️ Username: @{message.from_user.username}\n▪️ ID: {message.from_user.id}")

# Запуск бота
bot.polling(none_stop=True)
