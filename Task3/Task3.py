# #Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
              
listnum = []
for i in range(randint(5, 20)): 
    listnum.append(randint(0, 20))

print(f'Сгенерированный список: {listnum}')

newlist =[]
for j in range(len(listnum)):
    for k in range(len(listnum)):
        if j != k and listnum[j] == listnum[k]:
            break
    else:                           # else относится к циклу и будет выполнятся только 1 раз и в последней итерации
        newlist.append(listnum[j])

print(f'Список с исключением повторяющихся элементов: {newlist}')




# Альтернативные решения

# N = int(input())
# list = []
# for i in range(1,N+1):
#     a = randint(-N,N+1)
#     list.append(a)
# print(list)

# newlist = []
# for i in list:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)

# b = [1, 1, 2, 3, 3, 4, 5]
# a = []
# for i in b:
#     if b.count(i) == 1:
#          a.append(i)

# print(a)

# inp = list(map(int, input('Insert numbrers: ').split()))
# print(set(inp))