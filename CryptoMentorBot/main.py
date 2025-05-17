import telebot
from keep_alive import keep_alive

bot = telebot.TeleBot("7831525545:AAE2ndGlPoZ1vQWHmPW24aKDwCoWrhguP-g", parse_mode="Markdown")

admin_id = 7928644968  # твой Telegram ID

@bot.message_handler(commands=["start"])
def send_welcome(message):
    chat_id = message.chat.id
    user = message.from_user

    # Уведомление админу
    notify = (
        f"👤 *New user launched the bot!*\n"
        f"▪️ Name: {user.first_name}\n"
        f"▪️ Username: @{user.username if user.username else '—'}\n"
        f"▪️ ID: `{user.id}`"
    )
    bot.send_message(admin_id, notify)

    # Текст пользователю
    caption = (
        "✋🏼Glad to see you on our👉🏼 [CHANNEL](https://t.me/+V8FKWfygiRY4Nzcx)👈🏼\n\n"
        "We are the [«CRYPTO MENTOR | KIT grp»](https://t.me/+V8FKWfygiRY4Nzcx) community💎\n\n"
        "*📊 Our team is based on Futures market analysis.*\n"
        "*The winning percentage of our Signals is now 97%* ✅\n\n"
        "📲 [Join now](https://t.me/Kit_futures?text=I%20WANT%20SIGNAL)"
    )

    # Кнопки
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(
        telebot.types.InlineKeyboardButton("CHANNEL📲", url="https://t.me/+V8FKWfygiRY4Nzcx"),
        telebot.types.InlineKeyboardButton("GET FREE SIGNAL🤑", url="https://t.me/Kit_futures?text=I%20WANT%20SIGNAL")
    )

    bot.send_message(chat_id, caption, reply_markup=markup)

keep_alive()
bot.polling()
