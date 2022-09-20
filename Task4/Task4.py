#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint
import itertools

k = int(input('Введите значение степени: '))

def ratios(k):                                        # рандомим коэффициенты
    ratios = [randint(1, 10) for i in range (k + 1)]  
    print(f'Сгенерированный список коэффициентов: {ratios}')
    return ratios

def polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '')]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')

ratios1 = ratios(k)
polynom1 = polynomial(k, ratios1)
print(polynom1)

with open('Polynomial.txt', 'w') as data:
    data.write(polynom1)