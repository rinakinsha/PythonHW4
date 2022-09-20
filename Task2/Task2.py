#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def Factorization(n):
    list = []
    a = 2                 # начинаем с 2, т.к. 1 не считается простым числом
    while a * a <= n:     # при таком условии исключит из списка 1
        if n % a == 0:
            list.append(a)
            n //= a
        else:
            a += 1
    if a > 1:
        list.append(n)
    return list

N = int(input('Введите натуральное число: '))

print(f'Простые множители числа {N}: {Factorization(N)}')

# Альтернативное решение
# num = int(input("Введите число: "))
# i = 2 # первое простое число
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old} приведены в списке: {lst}")
