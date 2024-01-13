import math


def task1():
    p = 1
    while 1:
        e = int(input())
        if e == 0:
            break
        p *= e
    print('the product of a sequence =', p)


def task2():
    n = int(input())
    s = 0
    
    if n == s:
        print("Number is perfect")
    else:
        print("Number isn't perfect")


def task3():
    p = 1
    while 1:
        e = int(input())
        if e == 0:
            break
        if e < 0:
            p *= e
    print('the product of a sequence of negative numbers =', p)


def task4():
    n = []
    while 1:
        e = int(input())
        n.append(e)
        if e == 0:
            break
    i1 = n.index(-5)
    i2 = n.index(5)
    if i1 < i2:
        for i in range(i1+1, i2):
            print(n[i], end=' ')
    else:
        for i in range(i2+1, i1):
            print(n[i], end=' ')
    print()


def task5():
    n, m = int(input()), int(input())
    s = 0
    for i in range(1, n+1):
        for j in range(m):
            i *= i
        s += i
    print('the sum of numbers from 1 to N raised to the power of M =', s)


def task6():
    a, b = int(input()), int(input())
    res = 0
    for i in range(10):
        res += b - a
        b *= 1.03
    print('Student needs', res, 'tg extra, so he could live with scholarship')
    print('Overall he needs', res+10*a, 'tg to live 10 months')


def task7():
    s, a, b = int(input()), int(input()), int(input())
    months = 0
    while s > 0:
        s -= b
        s += a
        b *= 1.03
        months += 1
    print('the student can live', months, 'months using only the savings and the scholarship')


def task8():
    print('All four-digit numbers in which all digits are different:')
    for i in range(1000, 10000):
        num = str(i)
        if len(set(num)) == 4:
            print(int(i), end=' ')
    print()


def task9():
    n = int(input())
    print('All', n, 'digit(s) Armstrong numbers:')
    for i in range(10**(n-1), 10**n):
        s = 0
        num = i
        for j in range(n):
            s += (num % 10)**n
            num //= 10
        if s == i:
            print(i, end=' ')
    print()


def task10():
    print('Numbers in the range from 1 to 1000 that have exactly five divisors:')
    for i in range(1, 1001):
        div = 0
        for j in range(1, i + 1):
            if i % j == 0:
                div += 1
        if div == 5:
            print(i, end=' ')
    print()


def task11():
    n = int(input('Enter a max number: '))
    print('All numbers divisible by seven,\nwhere the sum of their digits is\nalso divisible by seven')
    for i in range(1, n+1):
        if i % 7 == 0:
            sm = sum(int(d) for d in str(i))
            if sm % 7 == 0:
                print(i, end=' ')
    print()


def task12():
    n = int(input())
    str_n = str(n)
    for d in range(10):
        str_d = str(d)
        c = 0
        for i in str_n:
            if i == str_d:
                c += 1
        if c > 0:
            print('Digit', d, 'occurs', c, 'time(s)')


def task13():
    x = int(input('Enter x: '))
    n = int(input('Enter number of iterations: '))
    res = 0
    odd_n = 1
    for i in range(n):
        res += (1/odd_n)*((x-1)/(x+1))**odd_n
        odd_n += 2
    print(res)


def task14():
    x = int(input('Enter x: '))
    n = int(input('Enter number of iterations: '))
    res = 0
    sign = -1
    for i in range(1, n+1):
        res += sign*(math.cos(i*x)/i**2)
        sign *= -1
    print(res)


def task15():
    x = int(input('Enter x: '))
    n = int(input('Enter number of iterations: '))
    res = 0
    sign = 1
    i = 3
    ii = 1
    for j in range(1, n+1):
        res += sign * ((x ** i) / (ii*i))
        ii = i
        i += 2
        sign *= -1
    print(res)


while 1:
    task_num = int(input('Enter the number of task to check: '))
    match task_num:
        case 1:
            task1()
        case 2:
            task2()
        case 3:
            task3()
        case 4:
            task4()
        case 5:
            task5()
        case 6:
            task6()
        case 7:
            task7()
        case 8:
            task8()
        case 9:
            task9()
        case 10:
            task10()
        case 11:
            task11()
        case 12:
            task12()
        case 13:
            task13()
        case 14:
            task14()
        case 15:
            task15()
        case _:
            print('Invalid number of task')
            break
