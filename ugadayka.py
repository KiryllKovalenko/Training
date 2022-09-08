from random import randint
a = 0 # число попыток
x = randint(1, 20)  # случайное число в диапазоне 1-20
while a <= 2: # Увеличить число попыток

    b = int(input("Введите число от 1 до 20: "))
    while True:
        a += 1
        if b < x:
            print("Ты ввёл число, меньше загаданного")
            break
        elif b > x:
            print("Ты ввёл число, больше загаданного")
            break
        elif b == x:
            print(f'Ты угадал мое число, использовав {a} попытки!')
            break


else:
    a == 3
    print("Твои попытки закончились!")



