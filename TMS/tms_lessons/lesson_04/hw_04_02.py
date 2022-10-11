"""Ex. 2
Дан словарь. Создать новый словарь, поменяв местами ключ и значение
"""
dct = {0: 'муж',1: 'жен'}
res = {key: value for value, key in dct.items()}
assert res == {'муж': 0, 'жен': 1}
print(res)
