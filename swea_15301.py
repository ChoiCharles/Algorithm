import sys
sys.stdin = open('swea_15301_input.txt', 'r')

def asdf(a):
    global cnt
    if c1[a] != 0:
        cnt += 1
        asdf(c1[a])
    if c2[a] != 0:
        cnt += 1
        asdf(c2[a])

T = int(input())
for test_case in range(1, T + 1):
    e, n = map(int, input().split())
    lst = list(map(int, input().split()))
    parent = []
    for i in range(1, e + 1):
        parent.append(i)
    c1 = [0] * (e + 2)
    c2 = [0] * (e + 2)
    for i in range(e):
        p = lst.pop(0)
        c = lst.pop(0)
        if c1[p] == 0:
            c1[p] = c
        else:
            c2[p] = c
    cnt = 1
    asdf(n)
    print(f'#{test_case} {cnt}')