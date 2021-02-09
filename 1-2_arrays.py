print('-----LISTCOMP-----')
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)  #В отличиче от zip - все получится

print('-----GENEXP-----')
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = ((color, size) for color in colors for size in sizes) #generator object in ()
print(tshirts)

print('-----TUPLES-----')
travelers_ids = [('USA', 3123214), ('RUSSIA', 39434,), ('UK', 2312421)]
for country, passport in travelers_ids:
    print(country)  #Печатаем только страну, passport - фиктивная переменная, если интересует только один элемент кортежа

coordinates = (12321312, -342342342)
coord_1, coord_2 = coordinates
print(coord_1, coord_2) #Автоматическое присваивание из кортежа

print('-----*rest-----')
a, b, *rest = range(5)  #0 1 [2, 3, 4]
print(a, b, rest)       #0 [1, 2] 3 4
a,*rest, b, c = range(5)
print(a, rest, b, c)

print('-----NAMED TUPLE-----')
from collections import namedtuple
City = namedtuple('City', 'name counrty population coordinates')    #Как будто объявили класс
tokyo = City('Tokyo', 'JP', 36.933, (35.68, 139.691))
print(tokyo)
print(tokyo.name)
print(tokyo.population)
print(tokyo.coordinates)

print('-----NESTED LISTS-----')
board = [['_'] * 3 for i in range(3)]
print(board)
board[0][2], board[1][2], board[2][1] = 'O', 'X', 'X'
print(board)

print('-----WOW tuple-----')
t = (1, 2, [30, 40])
try:
    t[2] += [50, 60]
except TypeError as e:
    print(e)
    print(t)    #Кидает ошибку и тем не менее изменяет tuple!

print('-----BISECT.INSORT-----')
import bisect   #Поддерживает последовательность отсортированной
import random

size = 8
random.seed(1729)

my_list = []
for i in range(size):
    new_item = random.randrange(size * 2)
    bisect.insort(my_list, new_item)
    print(new_item, ' -> ', my_list)

print('-----DEQUE-----')
from collections import deque
dq = deque(range(10),maxlen=10)
print(dq)
dq.rotate(3)    #3 элемента удаляются с правого конца и добавляются с левого
print(dq)
dq.rotate(-4)   #4 элемента удаляются с левого конца и добавляются с правого
print(dq)
dq.appendleft(-1)   #Добавить элемент слева
print(dq)
dq.extend([11, 20, 35, 40]) #Добавить элемента справа
print(dq)
dq.extendleft([15, 25]) #Добавляет элементы слева в противоположном порядке (т.е. добпаляеи последовательно в левый конец - сначала 15, потом 25)
print(dq)
