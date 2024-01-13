import math
x, y, z = map(int, input('Enter numbers x, y and z: ').split())
a = (3+math.exp(y-1))/(1+(x**2)*abs(y-math.tan(z)))
b = 1+abs(y-x)+(y-x)**2/2+abs(y-x)**3/3
print('a =', a, '\nb =', b)
