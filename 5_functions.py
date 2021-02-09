print('-----FUNCTIONS-----')
print('listcomp и gencopm могут сделать то же самое, что map, filter и reduce')

import math
fact = [math.factorial(n) for n in range(6)]
print(fact)
fact = [math.factorial(n) for n in range(6) if n % 2 == 0]
print(fact)
summ = sum(range(5000)) #Аналог reduce
print(summ)
print('all - True если каждый элемент iterable "похож"',
      'any - если хотя бы один', sep='\n')

print('-----LAMBDA-----')
fruits = ['apple', 'cherry', 'banana']
print(sorted(fruits, key=lambda x: x[::-1]))    #Сортировка списка слов в обратном порядке

print('-----ITEMGETTER-----')
from operator import itemgetter
metro_data = [
    ('Tokyo', 'JP', 36.933),
    ('Delhi NCR', 'IN', 21.395),
    ('Mexico City', 'MX', 20.142),
    ('New-York-Newark', 'US', 20.104),
    ('Sao Paulo', 'BR', 19.649)
]
for city in sorted(metro_data, key=itemgetter(1)):      #Сортировка по аббревиатуре страны
    print(city)
print('---------------')
for city in metro_data:
    print(itemgetter(1,0)(city))    #Вывод второго и первого элемента последовательности

