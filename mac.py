import random
lev = int(input("сколько уровней вы бы хотели? "))
c1, c2 = map(int, input("с каким соотношением вы бы хотели выпадение левого пути? В ответе нужно два число через пробел").split())
a = 0
ch = [-1] * c1 + [1] * c2)
for i in range(lvl):
    a += int(ch[random.randint(0, len(ch))])

print('корзина номер', 2 ** lvl - a, 'вас ждет на этот раз')
