import datetime
import telebot
from telebot import types

# Встановлюємо дві дати
date1 = datetime.date(2024, 9, 8)
date2 = datetime.date.today()

# Віднімаємо дати
difference = date2 - date1

num = ( difference.days - 1) // 7

print(num)

if(num % 2 == 0):
    print("знаменник")
    
else:
    print("чисельник")

num2 = (difference.days - 1) % 7
 
schedule1pchis = [" (1 пара) Фізкультура (2 пара) Аллебра (практична) (3 пара) АіП (практична) "," (1 пара) Алгебра (пракчтична) (3 пара) Алгебра (лекція) (4 пара) Фізика (лабораторна) "," (2 пара) АіП (лабораторна) (3 пара) Фізика (лекція) ", " (1 пара) Історія (лекція) (2 пара) Дискретна (лекція) (3 пара) Англійська ", " (1 пара) Дискретна (практична) (2 пара) АіП (лекція) " ]
schedule1pznam = [" (1 пара) Фізкультура (2 пара) Аллебра (практична) (3 пара) АіП (практична) "," (2 пара) Дискретна (лабораторна) (3 пара) Алгебра (лекція) (4 пара) Фізика (лабораторна) "," (2 пара) АіП (лабораторна) (3 пара) Фізика (лекція) ", " (2 пара) Дискретна (лекція) (3 пара) Англійська ", " (1 пара) Дискретна (практична) (2 пара) АіП (лекція) (3 пара) Історія (практична) " ]



print(num2)
for i in  range(6):
    if(num % 2 == 0):
        if num2 == 5 and num // 5 == 0:
            now = schedule1pchis[num % 5]
            tomorrow = schedule1pchis[0]
            
            break
        elif num2 == 5 and num // 5:

            now = schedule1pznam[num % 5]
            tomorrow = schedule1pchis[0]
            
            break
        elif num2 == i:
            now = schedule1pchis[i]
            tomorrow = schedule1pchis[i + 1]
            break
        elif num2 == 6:

            now = "Віддихай Неділя"
            tomorrow = schedule1pchis[0]
            break  

    elif(num % 2 != 0):
        if num2 == 5 and num // 5 == 0:

            now = schedule1pchis[num % 5]
            tomorrow = schedule1pznam[0]
            break
        elif num2 == 5 and num // 5:

            now = schedule1pznam[num % 5]
            tomorrow = schedule1pznam[0]
            break
        
        elif num2 == i:

            now = schedule1pchis[i]
            tomorrow = schedule1pznam[i + 1]
            break
            
        elif num2 == 6:

            now = "Віддихай Неділя"
            tomorrow = schedule1pznam[0]
            break  
print(now)

TOKEN = '7261206490:AAEPdVxlFq49URUc8ocS3RzQOHjQg1EAtL8'
bot = telebot.TeleBot(TOKEN)

bot.set_my_commands([
    types.BotCommand("/start", "Привітання"),
    types.BotCommand("/schedule", "Дізнатися розклад для першої підгрупи"),
])

@bot.message_handler(commands=['schedule'])
def send_schedule(message):
    bot.reply_to(message, "Ось розклад на сьогодні")
    bot.send_message(message.chat.id, now)
    bot.send_message(message.chat.id, "Ось розклад на завтра")
    bot.send_message(message.chat.id, tomorrow)
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт я можу дати тобі розклад занять на сьогодні")
bot.polling()
