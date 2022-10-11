"""Ex 5. Реализовать вычисление факториала с помощью цикла while и for.
Продумать область допустимых значений.
Добавить проверки, исключаютщие бесконечный цикл.
Написать тесты на различные варианты.
"""

n_1 = int(input())

factorial_1 = 1
while n_1 > 1:
    factorial_1 *= n_1
    n_1 -= 1

print(factorial_1)

n_2 = int(input())

factorial_2 = 1

for i in range(2, n_2 + 1):
    factorial_2 *= i

print(factorial_2)