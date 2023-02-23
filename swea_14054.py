import sys
sys.stdin = open("swea_14054_input.txt", "r")

from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    q = deque()
    for i in range(1, n + 1):
        a = lst.pop(0)
        q.append([i, a])
    cnt = 0
    while cnt < n - 1:
        a = q.popleft()
        if a[0] != -1:
            a[1] = a[1] // 2
        if a[0] == -1:
            q.append(a)
        elif a[1] == 0:
            try:
                a = lst.pop(0)
                i += 1
                q.append([i, a])
            except:
                cnt += 1
                q.append([-1, 0])
        else:
            q.append(a)
    while 1:
        a = q.pop()
        if a[1] != 0:
            break
    print(f'#{test_case} {a[0]}')