# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Если посередине один элемент, то квадрат числа.

def is_int(value):  # Проверка введенного значения на целое число
    try:
        int(value)
        return True
    except ValueError:
        return False

N = input('Введите длину списка: ')

while not is_int(N) or int(N) < 0 or int(N) == 0:  # Проверка условий для введенного значения
    if not is_int(N):
        print('Введено не целое число')
        N = input('Введите целое число: ')
        continue
    elif int(N) < 0:
        print('Длина списка не может быть отрицательным числом')
        N = input('Введите целое положительное число больше единицы: ')
    elif int(N) == 0:
        print('При пустом списке нет элементов для выполнения условия задачи')
        N = input('Введите целое положительное число больше единицы: ')

N = int(N)

import random

list_random = []
for i in range(N):
    list_random.append(random.randint(0, 10))
print('Случайно сгенерированный список:')
print(list_random)

if N % 2 == 0:
    length = int(N / 2)
else:
    length = int(N / 2 + 1)


for i in range(length):
    print(f'{list_random[i] * list_random[N - i - 1]}', end=' ')

