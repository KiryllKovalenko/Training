"""Ex. 3
Добавить в ex.2 бесконечный цикл.
Выход из цикла сделать через ввод симолов "Q", "q"
"""

a = 1
while a==1:
    age = int(input('Введите ваш возраст: '))
    name = input('Введите ваше имя: ')
    if name == 'Q' or name == 'q':
        break
    if age <= 0:
        print("Ошибка, повторите ввод")
    elif age < 10:
        print(f"Привет, малыш {name}!")
    elif age <18:
        print(f"Как дела {name}?")
    elif age <=120:
        print(f"Что желаете {name}?")
    else:
        print(f"{name}, вы лжете - столько не живут")
