import telebot
from functions import get_subjects
from mongodb import collection


bot = telebot.TeleBot('1333094929:AAHMZ52Hzx2heoY7c5yINLsUXG-OkXNTE1E')





@bot.message_handler(commands=['start'])
def repeat_all(message):
        bot.send_message(message.chat.id, "Привет, я бот для расписания")

@bot.message_handler(commands=['timetable'])
def repeat_all_messages(message):
        a = "1 пара  08:30 - 10:05 "  + \
            "\n2 пара  10:25 - 12:00 " + \
            "\n3 пара  12:20 - 13:55"   + \
            "\n4 пара  14:15 - 15:55" + \
            "\n5 пара  08:30 - 17:45"
        bot.send_message(message.chat.id, a)




@bot.message_handler(commands=['monday'])
def monday(message):
    results = collection.find({"day": "monday"})
    timetable = get_subjects(results)
    bot.send_message(message.chat.id, "Понедельник" + "\n" + "\n" + timetable)

@bot.message_handler(commands=['tuesday'])
def tuesday(message):
    results = collection.find({"day": "tuesday"})
    timetable = get_subjects(results)
    bot.send_message(message.chat.id, "Вторник" + "\n" + "\n" + timetable)

@bot.message_handler(commands=['wednesday'])
def wednesday(message):
    results = collection.find({"day": "wednesday"})
    timetable = get_subjects(results)
    bot.send_message(message.chat.id, "Среда" + "\n" + "\n" + timetable)

@bot.message_handler(commands=['thursday'])
def thursday(message):
    results = collection.find({"day": "thursday"})
    timetable = get_subjects(results)
    bot.send_message(message.chat.id, "Четверг" + "\n" + "\n" + timetable)

@bot.message_handler(commands=['friday'])
def friday(message):
    results = collection.find({"day": "friday"})
    timetable = get_subjects(results)
    bot.send_message(message.chat.id, "Пятница" + "\n" + "\n" + timetable)












if __name__ == '__main__':
    bot.polling(none_stop=True)
