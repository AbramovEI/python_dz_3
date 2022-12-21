# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16];           - [2, 3, 5, 6] => [12, 15]


print('Введите количеств элементов списка = ')
n = int(input())
list1 = list()
print()
for i in range (n):
    k = int(input())
    list1.append(k)
print(list1)

list2 = list()
l = len(list1)//2 + 1 if len(list1) % 2 != 0 else len(list1)//2
list2 = [list1[i]*list1[len(list1)-i-1] for i in range(l)]

print()

print(list2)

