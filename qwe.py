import math

esp = 0.0001
sum = 0
x = float(range(0.6, 1.1, 0.25))
n = 0
step = 0.25

while x <= 1.1:
    for k in range(10, 16):
        summ = 0
        for k in range(1, n + 1):
            summ = math.cos(x*k)
        f = math.sqrt(x) + (1/9) * summ


    x += step