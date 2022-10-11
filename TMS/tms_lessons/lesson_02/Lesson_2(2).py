#Ex. 2
#Есть список NUMBERS, содержащий повторяющиеся целые числа.
#С помощью словаря (dict) отфильтровать его и получить новый список с уникальными числами.

NUMBERS = [1,1,1,2,2,2,3,3,3,4,5,6,7,7,8,8,0,9,9]
numbers_dictionary = dict.fromkeys(NUMBERS, 'unique numbers')
print(numbers_dictionary)