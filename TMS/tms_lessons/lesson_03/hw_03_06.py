"""Ex.6
Написать программу в которой нужно будет угадывать число.
Продумать диапазон чисел (будут жестко заданы или задаваться самим пользователем)
"""
from random import randint
a = 0 # число попыток
x = randint(1, 20)  # случайное число в диапазоне 1-20
while a <= 10: # Увеличить число попыток
    b = int(input("Введите число от 1 до 20: "))
    a += 1
    if b < x:
        print("Ты ввёл число, меньше загаданного")

    elif b > x:
        print("Ты ввёл число, больше загаданного")

    elif b == x:
        print(f'Ты угадал мое число, использовав {a} попытки!')
        break
else:
    print("Твои попытки закончились!")
