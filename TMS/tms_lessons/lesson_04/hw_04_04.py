"""Ex. 4
Ф-я принимает список целых чисел и возвращает минимальное число, максимальное число, среднее-арифметическое.
"""
new_list = [i for i in range(1,20)]
def foo():
    number_min = min(new_list)
    number_max = max(new_list)
    arithmetic_mean = len(new_list)/2
    print(number_min, number_max, arithmetic_mean, sep="\n")
foo()