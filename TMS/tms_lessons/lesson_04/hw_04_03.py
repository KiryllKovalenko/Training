"""Ex. 3
На вход функции подается натуральное число n.
Напишите программу, использующую списочное выражение, которая создает список содержащий квадраты чисел от 1 до n,
а затем выводит его элементы построчно, то есть каждый на отдельной строке.
"""

n_1 = int(input('Введите число: '))
summ_1 = [x ** 2 for x in range(1, n_1+1)]
for x in summ_1:
    print(x)