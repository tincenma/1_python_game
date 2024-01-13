import math
x, y, z = map(int, input('Enter numbers x, y and z: ').split())
a = (1+y)*(x+y/(x**2+4))/(math.exp(-x-2)+1/(x**2+4))
b = (1+math.cos(y-2))/(x**4/2+(math.sin(z))**2)
print('a =', a, '\nb =', b)
