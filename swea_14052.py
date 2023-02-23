import sys
sys.stdin = open("swea_14052_input.txt", "r")

from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def asdf(y, x):
    global cnt
    flag = 0
    q = deque()
    q.append([y, x])
    arr[y][x] = 0
    while 1:
        try:
            y, x = q.popleft()
        except:
            cnt = 0
            break
        for i in range(4):
            if arr[y + dy[i]][x + dx[i]] == '0':
                q.append([y + dy[i], x + dx[i]])
                arr[y + dy[i]][x + dx[i]] = arr[y][x] + 1
            elif arr[y + dy[i]][x + dx[i]] == '3':
                cnt = arr[y][x]
                flag = 1
                break
        if flag == 1:
            break


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [['1'] * (n + 2)]
    for i in range(n):
        a = list(input())
        a = ['1'] + a + ['1']
        arr.append(a)
    arr += [['1'] * (n + 2)]
    flag = -1
    for i in range(n + 2):
        for j in range(n + 2):
            if arr[i][j] == '2':
                y, x = i, j
                flag = 0
                break
        if flag == 0:
            break
    cnt = 0
    asdf(y, x)
    print(f'#{test_case} {cnt}')
