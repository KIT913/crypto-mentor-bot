import telebot

bot = telebot.TeleBot("7831525545:AAE2ndGlPoZ1vQWHmPW24aKDwCoWrhguP-g")
admin_id = 7928644968

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user = message.from_user
    text = (
        "👋🏼 Glad to see you on our👉🏼 <b>CHANNEL</b> 👈🏼\n\n"
        "We are the «<b>CRYPTO MENTOR | KIT grp</b>» community💎\n\n"
        "📊 Our team is based on Futures market analysis.\n"
        "The winning percentage of our Signals is now <b>97%</b> ✅\n\n"
        "📲 <a href='https://t.me/+lxFWpKJ49J8wN2Vh'>Join now</a>"
    )
    bot.send_message(message.chat.id, text, parse_mode='HTML')
    
    # Уведомление админу
    notify = f"👤 New user launched the bot!\n▪️ Name: {user.first_name}\n▪️ Username: @{user.username}\n▪️ ID: {user.id}"
    bot.send_message(admin_id, notify)

bot.polling()
