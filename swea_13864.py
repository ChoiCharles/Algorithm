import sys
sys.stdin = open("swea_13864_input.txt", "r")

def asdf(a, b):
    if a[1] == b[1]:
        return a
    elif a[1] > b[1]:
        if a[1] == 3 and b[1] == 1:
            return b
        else:
            return a
    elif a[1] < b[1]:
        if a[1] == 1 and b[1] == 3:
            return a
        else:
            return b

def asdfg(i, j):
    if i == j:
        return
    if j - i == 1:
        a = asdf(tup[i], tup[j])
        if a == tup[i]:
            tup[j] = a
        elif a == tup[j]:
            tup[i] = a
        return
    asdfg(i, (i+j)//2)
    asdfg((i+j)//2+1, j)
    a = asdf(tup[i], tup[j])
    if a == tup[i]:
        tup[j] = a
    elif a == tup[j]:
        tup[i] = a
    return


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    dic = {i: l for i, l in enumerate(lst)}
    tup = list(zip(dic.keys(), dic.values()))

    asdfg(0, n-1)


    print(f'#{test_case} {tup[0][0]+1}')