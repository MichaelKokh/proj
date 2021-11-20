import random
import telebot
from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)
controller = {}
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, """
    Вы здесь чтобы протестировать мою доску гальтона? Feel free to write anything, you want.
    Я хочу услышать от вас в одном сообщении через пробел количество уровней и два числа - коэфициента выбора левого и правго пути через пробел
    При желании, можно четвертым числом указать количество ворот на одном уровне.
    """)
    user_id = message.from_user.id
    controller[user_id] = 'start'

@bot.message_handler(content_types=['text'])
def start(message):
    user_id = message.from_user.id
    user_choice = message.text
    user_state = controller.get(user_id, 'start') # Если вдруг такой user_id не сохранен, то считаем, что статус = start
    if user_state == 'start':
        answer = start_handler(user_id, user_choice)
    bot.send_message(message.from_user.id, answer)

def start_handler(user_id, user_choice):
    c3 = 0
    try:
        lev, c1, c2, c3 = map(int, user_choice.split())
    except ValueError:
        lev, c1, c2 = map(int, user_choice.split())
    a = 0
    ch = [-1] * c1 + [1] * c2
    for i in range(lev):
        a += int(ch[random.randint(0, len(ch)-1)])
    if (c3):
        answer =  """корзина номер {} вас ждет на этот раз""".format((c3)**lev + a)
    else:
        answer =   """корзина номер {} вас ждет на этот раз""".format(2**lev + a)
    return answer
    #bot.send_message(user_id, answer)
bot.polling()
