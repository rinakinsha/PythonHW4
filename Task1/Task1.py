# Вычислить число Пи c заданной точностью d

a = int(input('Введите желаемую точность числа Пи: '))

s = 1
pi = 0
for s in range(1, 1000000):         #1000000 - для более точного вычисления числа Пи (НО! Чем больше 0 - тем медленне работает программа :( )
    pi = pi+4*((-1)**(s+1))/(2*s-1) #Вычисление числа Пи по ряду Лейбница (максимум - 16 знаков после запятой)
print(round(pi, a))

#Решение через встроенную функцию
#from math import pi

#a = int(input('Введите желаемую точность числа Пи: '))
#print(f'Число Пи с заданной точностью {a} равно {round(pi,a)}')