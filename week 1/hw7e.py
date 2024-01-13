import math
x, y, z = map(int, input('Enter numbers x, y and z: ').split())
a = (1+math.sin(x+y)**2)/(2+abs(x-(2*x)/(1+x**2*y**2)))+x
b = math.cos(math.atan(1/z))**2
print('a =', a, '\nb =', b)
