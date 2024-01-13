import math
x, y, z = map(int, input('Enter numbers x, y and z: ').split())
a = (2*math.cos(x-math.pi/6))/(1/2+(math.sin(y))**2)
b = 1+(z**2)/(3+z**2/5)
print('a =', a, '\nb =', b)
