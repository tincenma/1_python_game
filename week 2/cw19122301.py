n = int(input())
for i in range(1, n + 1):
    if i == (i ** 2) % 10:
        print(i, end=' ')
