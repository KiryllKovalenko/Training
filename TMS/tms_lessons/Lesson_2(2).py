NUMBERS = [1,1,1,2,2,2,3,3,3,4,5,6,7,7,8,8,0,9,9]
spisok = {
    'a': NUMBERS

}
b = set(spisok['a'])
assert b == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}