"""Ex. 1
Ввести предложение, состоящее из двух слов. Поменять местами слова, добавить "!" в начало и конец, слова разделить
3 символами (" ", "!", " ")"""
s = input('Введите предложение из двух слов: ')
s = s.split(' ')
s = s[::-1]
s = ' '.join(s)
print(s, end='\n')

