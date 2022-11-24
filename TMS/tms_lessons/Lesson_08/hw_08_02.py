from time import sleep


class Auto:

    def __init__(self, brand, age, mark, color='blue', weight=1):
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

a = Auto('bmv', 17, 'x7')

a.move()
a.stop()
a.birtrhday()
print(a.age)

class Truck(Auto):

    def __int__(self, brand, age, mark, max_load=2.1):

        super().__init__(age, brand, mark)
        self.max_load = max_load

    def move(self):
        print('Attention')
        super().move()

    def load(self):
        sleep(1)
        print('load')
        sleep(1)

b = Truck('bmv', 17, 'x7')
b.move()
b.birtrhday()
b.load()
print(b.age)

class Car(Auto):

    def __int__(self, brand, age, mark, max_speed):
        super().__init__(age, brand, mark)
        self.max_speed = max_speed


    def move(self):
        max_speed = 160
        print('Attention')
        super().move()
        print('max speed is', max_speed)

c = Car('bmv', 17, 'x7')
c.move()
c.stop()
c.birtrhday()

print(c.age)