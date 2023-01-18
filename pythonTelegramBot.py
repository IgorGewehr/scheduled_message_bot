import telebot
import schedule
import time
import random
import datetime
import emoji
import asyncio

bot = telebot.TeleBot("5929920992:AAHhBJ9cfBQXR723vNb0ya0UGgMqBj-nnJQ")

def generate_message():
    percent1 = random.randint(92, 99)
    percent2 = random.randint(92, 99)
    percent3 = random.randint(92, 99)
    current_date = datetime.datetime.now()
    valid_date = current_date + datetime.timedelta(days=3)
    valid_date_formatted = valid_date.strftime("%d/%m")
    message = "`{} Jogos Atualizados e Vãlidos até Dia {}\n" \
              "{}Jogos 1, 4 e 9 - {}%\n"\
              "{}Jogos 6, 7 e10 - {}%\n"\
              "{}Jogos 3, 5 e 8 - {}%".format(emoji.emojize(':white_check_mark:'),valid_date_formatted,
                                              emoji.emojize(':fire:'),percent1,
                                              emoji.emojize(':fire:'),percent2,
                                              emoji.emojize(':fire:'),percent3)
    return message

@bot.message_handler(commands=['teste'])
def send_welcome(message):
    bot.reply_to(message, "Funcionando!")

@bot.message_handler(commands=['iniciar'])
def start_scheduled_message(message):
    bot.send_message(message.chat.id, generate_message())
    schedule.every(3).days.do(send_scheduled_message, message)


def send_scheduled_message(message):
    bot.send_message(message.chat.id, generate_message())

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Adiciona a funcao para rodar o schedule

bot.polling()
run_scheduler()