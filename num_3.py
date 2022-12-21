# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:  - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

print('Введите количеств элементов списка = ')
n = int(input())
list1 = list()
print()
for i in range (n):
    k = float(input())
    list1.append(k)

list2 =list()
list2 = [round(list1[i]* 100 % 100) for i in range (n)]
list2.remove(0)

max = 0
sum = 0
for i in range (len(list2)):
    if list2[i] > max:
        max = list2[i]
        min = list2[0]
    elif list2[i] < min:
        min = list2[i]

sum = max/100 - min/100

print('разность дробных значений = ')
print(sum)
