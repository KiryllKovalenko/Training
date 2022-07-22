from random import randint
a = 0 # число попыток

while a <= 2:
    x = randint(1, 6)  # загаданное число
    b = int(input("Введите число от 1 до 100: "))
    while True:
        a += 1
        if b < x:
            print("Ты ввёл число, меньше загаданного")
        elif b > x:
            print("Ты ввёл число, больше загаданного")
        elif b == x:
            print(f'Ты угадал мое число, использовав {a} попыток!')
else:
    a == 3
    print("Твои попытки закончились!")



