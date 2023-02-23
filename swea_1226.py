import sys
sys.stdin = open("swea_1226_input.txt", "r")

from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def asdf(y, x):
    global cnt
    q = deque()
    q.append([y, x])
    while 1:
        try:
            y, x = q.popleft()
        except:
            break
        arr[y][x] = 1
        for i in range(4):
            if arr[y + dy[i]][x + dx[i]] == 0:
                q.append([y + dy[i], x + dx[i]])
            elif arr[y + dy[i]][x + dx[i]] == 3:
                cnt += 1
                break
        if cnt > 0:
            break


T = 10
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    flag = -1
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                y, x = i, j
                flag = 0
                break
        if flag == 0:
            break
    cnt = 0
    asdf(y, x)
    if cnt > 0:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')