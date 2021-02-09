import collections
#Хэшируемый - имеет хэщ значение, которое не изменяется на протяжении всей жизни и допкускает сравнение с другимим объектами
print('-----HASH-----')
t1 = (1, 2, (30, 40))
print(hash(t1))

try:
    t2 = (1, 2, [30, 40]) #Хэшируемый - только если все его элементы хэшируемы
    print(hash(t2))         #Выдаст ощибку
except TypeError as e:
    print(e)

t3 = (1, 2, frozenset([30, 40]))
print(hash(t3))

print('-----DICT SETUP OPTIONS-----')
a = dict(one=1, two=2, three=3)
b = {'one':1, 'two':2, 'three':3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
print(a == b == c == d)

print('-----DICTCOMP-----')
CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'US'),
    (62, 'Indonesia'),
    (7, 'Russia'),
    (81, 'Japan')
]

country_code = {country: code for code, country in CODES}
print(country_code)

print('-----DEFAULT DICT-----')
from collections import defaultdict
d = defaultdict(list)   #Всегда нужно передавать аргумент в defaultdict - если ключа нет, то ему будет присвоен этот аргумент как пара-значение
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
print(d)

d = defaultdict(lambda: 3)  #Автоматически присвоить значение 3
d['three']                  #Этому ключу будет присвоено значение 3
print(d)

print('-----ORDEREDDICT-----')  #Хранит ключи в том порядке, в коротом они добавлялись
d = {'one':1, 'two':2, 'three':3}
print(d)

print('-----DICT COUNTER-----')  #С каждым ключом ассоциирован счетчик вхождений
ct = collections.Counter('adsadvascadcvdstcatdscad')
print(ct)
ct.update('asdadfdfasdfadf')
print('after update:', ct)
ct_mc = ct.most_common(3)   #Список из множеств наиболее частых элементов
print('most_common(3)', ct_mc)

print('-----MAPPINGPROXYTIME only reading-----')  #Делает объект неизменяемым
from types import MappingProxyType
d = {'one':1, 'two':2, 'three':3}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy['one'])
try:
    d_proxy['four'] = 4
except TypeError as e:
    print(e)
#А если так, то получится:
d['four'] = 4
print(d_proxy)  #Подтягивает изменение оригинального словаря
