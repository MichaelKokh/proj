from telebot import types
button_1 = types.KeyboardButton('ДА')
button_2 = types.KeyboardButton('НЕТ')
main_kb = types.ReplyKeyboardMarkup()
main_kb.add(button_1).add(button_2)
