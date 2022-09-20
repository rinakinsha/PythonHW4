# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

ffile1 = open('file1.txt', 'r')
ffile2 = open('file2.txt', 'r')
ffile3 = open('file3.txt', 'w')
file1 = ffile1.readline()
file2 = ffile2.readline()
for i in range(len(file1)):
    if file1[i-1] != '^':
        if file1[i].isnumeric():
            ffile3.write(str(int(file1[i])+int(file2[i])))
        else:
            ffile3.write(str(file1[i]))
    else:
        ffile3.write(str(file1[i]))
ffile1.close
ffile2.close
ffile3.close

with open('file1.txt', 'r') as data1:
    read_file1 = data1.read()
print(f'1-я запись многочлена: {read_file1}')

with open('file2.txt', 'r') as data2:
    read_file2 = data2.read()
print(f'2-я запись многочлена: {read_file2}')

print('Итог в файле file3')