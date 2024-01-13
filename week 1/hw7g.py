import math
x, y, z = map(int, input('Enter numbers x, y and z: ').split())
a = y+x/(y**2+abs(x**2/(y+x**3/3)))
b = 1+(math.tan(z/2))**2
print('a =', a, '\nb =', b)
