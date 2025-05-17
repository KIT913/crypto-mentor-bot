import telebot

bot = telebot.TeleBot("7831525545:AAE2ndGlPoZ1vQWHmPW24aKDwCoWrhguP-g")
admin_id = 7928644968

@bot.message_handler(commands=["start"])
def send_welcome(message):
    chat_id = message.chat.id
    user = message.from_user

    # Уведомление админу
    notify = (
        f"👤 New user launched the bot!\n"
        f"First name: {user.first_name} {user.last_name or ''}\n"
        f"Username: @{user.username}\n"
        f"ID: {user.id}"
    )
    bot.send_message(admin_id, notify)

    # Сообщение пользователю
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

bot.polling(none_stop=True)
