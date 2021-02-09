print('-----DECORATORS-----')
def deco(func):
    def inner():
        print('running inner()')
    return inner
print('--ДЕКОРАТОР ПРИНИМАЕТ ВНЕШНЮЮ ФУНКЦИЮ И ВОЗВРАЩАЕТ ВНУТРЕННЮЮ ФУНКЦИЮ, изменяя в ней внешнюю')
@deco
def target():
    print('running target()')

target()    #Задекорировав target() мы изменили ее поведение и теперь ее результатом является то, что возвращает декоратор deco
print('--Декораторы помечают функции, меняя/дополняя их поведение. Можно сказать - заменяют одну функцию другой')

print('-----NONLOCAL-----')
def make_averager():
    count = 0
    total = 0

    def averager():
        nonlocal count, total   #nonlocal требуется, чтобы не было ошибки, т.к. внутри ф-ии averager() count и total не определены
        count += 1
        total += 1
        return total/count

    return averager()