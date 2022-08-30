from math import sqrt, sin, e, pi
k = 1
x = 0.6
step = 0.25
summ = 0
while x <= 1.1:
    for n in range(10, 16):
        for k in range(1, n + 1):
            summ += (sin((k-1 / k + 1)**2)) + pow(e, sqrt(x / k))
        f = (pi/(x**(0.5))) + (3 / (x + 5)) * summ
        print(f'{x=} {n=} {f=}')
        summ = 0
    x += step