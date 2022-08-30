a = []
b = []
for i in range(1,101):

    if i%7 == 0:
        a.append(i)
b = a[:5]
print(a, b, sep='\n')
