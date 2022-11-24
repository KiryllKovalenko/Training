class Auto:

    def __init__(self, brand, age, color, mark, weight):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print('Move')

    def stop(self):
        print('Stop')

    def birtrhday(self):
        self.age += 1


a = Auto('bmv', 1, 'black', 'x7', 1.2)

a.move()
a.stop()
a.birtrhday()
print(a.age)
