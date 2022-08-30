import math
k = 1
x = 0.6
step = 0.25
summ = 0

while x <= 1.1:
    for n in range(10, 16):
        for k in range(1, n + 1):
            summ += math.cos(x * k)
        f = pow(math.e, x) + summ
        print(f'{x=} {n=} {f=}')
        summ = 0
    x += step












# f = e**x + sum math.cos(x*k)