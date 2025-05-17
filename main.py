import telebot
from keep_alive import keep_alive

API_TOKEN = "7831525545:AAE2ndGlPoZ1vQWHmPW24aKDwCoWrhguP-g"
admin_id = 7928644968

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    user = message.from_user
    notify = f"""
New user launched the bot!

Username: @{user.username}
ID: {user.id}
Name: {user.first_name} {user.last_name or ""}
"""

    bot.send_message(admin_id, notify)

    welcome_text = """👋🏼 Glad to see you on our👉🏼 CHANNEL👈🏼

We are the «CRYPTO MENTOR | KIT grp» community💎

📊 Our team is based on Futures market analysis.
The winning percentage of our Signals is now 97% ✅

📲 [Join now](https://t.me/Kit_futures?text=I%20WANT%20SIGNAL)
"""
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown")

keep_alive()
bot.polling()
