"""Ex. 2
Написать программу, которая получает имя и возраст пользователя, проверяет возраст и выдает приветственное сообщение
в зависимости от возраста:
- меньше нуля или ноль или не число: "Ошибка, повторите ввод"
- больше 0 до 10 не включая: "Привет, малыш {имя}!"
- от 10 до 18 включая: "Как дела {имя}?"
- больше 18 и включая 120: "Что желаете {имя}?"
- в противном случае: "{имя} вы лжете - столько не живут"
"""
age = int(input('Введите ваш возраст: '))
name = input('Введите ваше имя: ')
if age <= 0:
    print("ошибка, повторите ввод")
elif age < 10:
    print(f"Привет, малыш {name}!")
elif age <18:
    print(f"Как дела {name}?")
elif age <=120:
    print(f"Что желаете {name}?")
else:
    print(f"{name}, вы лжете - столько не живут")
