s = int(input("Введите сумму займа: "))
p = 0.2
n = int(input("Введите кол-во лет: "))

# m = месячная сумма
m = (s * p * pow((1 + p), n)) / (12*((1+p)**n)-1)
print("Месячная выплата = ", m)


# Сколько мы всего заплатим банку
s = int(input("Введите сумму займа: "))
p = 0.2
n = int(input("Введите кол-во лет: "))
y = ((s * p) * n) * 2
print("Столько вы заплатите банку за все время: ", y, "рублей")

# сколько денег мы переплатим банку
s = int(input("Введите сумму займа: "))
p = 0.2
n = int(input("Введите кол-во лет: "))

y = (s * p) * n
print("Столько мы переплатим банку: ", y)