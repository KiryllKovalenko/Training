import math

# Первая задача
a = int(input("Введите значение 'а': "))
y = ((a**2 / 3) + ((a**2 + 4) / 6) + (math.sqrt(a**2 + 4) / 4) + (math.sqrt(a**2 + 4)**3) / 4)
print("Значение 'y'= ", y)

# Вторая задача
x = int(input("Введите значение 'x': "))
y = (math.cos(x) + math.sin(x))
print ("Значение 'y' = ", y)

# вычисление тангенса и котангенса
sin_b = int(input("Введите значение 'sin b': "))
cos_B = int(input("Введите значение 'cos B': "))
tg = (math.sin(sin_b) / math.cos(cos_B))
ctg = (math.cos(cos_B) / math.sin(sin_b))
print ("Значение тангенса: ", tg )
print ("Значение котангенса: ", ctg)

#Третья задача
x = int(input("Введите значение 'x': "))
y = x**5 + x**4 + x**3 + x**2 + x + 1
print ("y = ", y)

# Четвертая задача

 # первое уравнение
a = int(input("Введите значение 'a': "))
c = int(input("Введите значение 'c': "))

y = (0.5 + math.pow(c, 2)) / (a + c)
print ("y = ", y)

# второе уравнение
a = int(input("Введите значение 'a': "))
b = int(input("Введите значение 'b': "))
c = int(input("Введите значение 'c': "))
y = (a + b) / b + (a + c / c + b)
print ("y = ", y)

# третье уравнение
x = int(input("Введите значение 'x': "))
y = math.sqrt(pow(math.cos(pow(x, 2)), 2)) + pow(math.sin(x*2 - 1), 2)
print("y = ", y)

# четвертое уравнение
x = int(input("Введите значение 'x': "))
y = pow((x * 5), 2) + ((x**2) * 3) + math.sqrt(1 + pow(math.sin(x), 2))
print ("y = ", y)