num_1 = 0
num_2 = 1
n = int(input("Номер элемента числа Фибоначчи: "))
i = 0
while i < n - 1:
    fib_summ = num_1 + num_2
    num_1 = num_2
    num_2 = fib_summ
    i = i + 1
    print(fib_summ)
print("Последнее число последовательности: ", fib_summ)