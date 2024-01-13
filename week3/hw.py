import itertools


def task1():
    def derangement(g_num, list_m):
        if g_num == 0:
            return 1
        elif g_num == 1:
            return 0
        elif g_num in list_m:
            return list_m[g_num]
        else:
            list_m[g_num] = (g_num - 1) * (derangement(g_num - 1, list_m) + derangement(g_num - 2, list_m))
            return list_m[g_num]
    memory = {}
    g = int(input('How many guests: '))
    print(derangement(g, memory))


def task2():
    students = []
    while 1:
        student = input()
        if student == '':
            break
        students.append(student)
    names = [i.split()[1] for i in students]
    name_set = list(set(names))
    count = [0]*len(name_set)
    for i in range(len(count)):
        count[i] = names.count(name_set[i])
    print(name_set[count.index(min(count))])


def task3():
    def cyclic_shift(T, start_pos):
        L = len(T)
        Ti = ""
        for j in range(L):
            Ti += T[(start_pos + j) % L]
        return Ti

    def is_magic_word(T, K_pos):
        L = len(T)
        count = 0
        for i in range(L):
            Ti = cyclic_shift(T, i)
            if Ti == T:
                count += 1
        return count == K_pos

    def count_magic_permutations(String):
        count = 0
        for p in itertools.permutations(range(N)):
            T = "".join(S[i] for i in p)
            if is_magic_word(T, K):
                count += 1
        return count

    N, K = map(int, input().split())
    S = []
    for _ in range(N):
        S.append(input())
    count_magic_permutations(S)


task3()
