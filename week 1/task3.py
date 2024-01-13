a, b = map(int, input().split())
res = (a+b)/2
if (res*10) % 10 != 0:
    print(res)
else:
    print(int(res))
