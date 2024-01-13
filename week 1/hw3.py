a, b = map(int, input('Enter numbers a and b: ').split())
if a > b and a % b == 0:
    print('b is a divisor of a')
elif b > a and b % a == 0:
    print('a is a divisor of b')
else:
    print('neither number is a divisor of the other')
