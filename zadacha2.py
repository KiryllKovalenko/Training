s = int(input("Введите сумму займа: "))
p = 0.2
n = int(input("Введите кол-во лет: "))

# m = месячная сумма
m = (s * p * pow((1 + p), n)) / (12*((1+p)**n-1))
print("Месячная выплата = ", f"{m:.4f}")


# Сколько мы всего заплатим банку
y1 = (m * 12) * n
print("Столько вы заплатите банку за все время: ", f"{y1:.4f}", "рублей")

# сколько денег мы переплатим банку

y2 = y1 - s
print("столько денег мы переплатим банку :", f"{y2:.4f}")
