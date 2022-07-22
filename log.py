import math

def my_sin(angle):
    esp  = 0.00000000001
    sum = 0
    next_part = 1
    n = 0

    angle_rad = math.radians(angle)

    while abs(next_part) > esp:
        next_part = pow(-1, n) * (pow(angle_rad, 2 * n +1)) / math.factorial(2 * n + 1)
        sum += next_part
        n += 1

    return sum


my_angle = int(input('Enter angle degree: '))
angle_sin = my_sin(my_angle)

#  sin function comparison

print('-------------------------------------------------')
print(f'My Python sin() function: {angle_sin}')
print(f'In-built Python sin() function: {math.sin(math.radians(my_angle))}')