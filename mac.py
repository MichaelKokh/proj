import random
import telebot
from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)
controller = {}
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, """
    вы здесь чтобы протестировать мою доску гальтона? feel free to write anything, you want.
    Я хочу услышать от вас в одном сообщении через пробел количество уровнеей и два числа - коэфициента выбора левого и правго пути через пробел
    """)
    user_id = message.from_user.id
    controller[user_id] = 'start'

@bot.message_handler(content_types=['text'])
def start(message):
    user_id = message.from_user.id
    user_choice = message.text
    user_state = controller.get(user_id, 'start') # Если вдруг такой user_id не сохранен, то считаем, что статус = start
    #answer = 'none'
    if user_state == 'start':
        answer = start_handler(user_id, user_choice)
    if user_state == 'teacher':
        answer = teacher_handler(user_id, user_choice)
    bot.send_message(message.from_user.id, answer)

def start_handler(user_id, user_choice):
    lev, c1, c2 = map(int, user_choice.split())
    a = 0
    ch = [-1] * c1 + [1] * c2
    for i in range(lev):
        a += int(ch[random.randint(0, len(ch)-1)])
    answer =  """корзина номер {} вас ждет на этот раз""".format(2**lev + a)
    bot.send_message(user_id, answer)
"""
lev = int(input("сколько уровней вы бы хотели? "))
c1, c2 = map(int, input("с каким соотношением вы бы хотели выпадение левого пути? В ответе нужно два число через пробел").split())
a = 0
ch = [-1] * c1 + [1] * c2)
for i in range(lvl):
    a += int(ch[random.randint(0, len(ch))])

print('корзина номер', 2 ** lvl - a, 'вас ждет на этот раз')
"""
bot.polling()
