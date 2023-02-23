import sys
sys.stdin = open("swea_14055_input.txt", "r")

from collections import deque

def bfs(s):
    global cnt, res, g, v
    q = deque()
    q.append((s, 0))
    while 1:
        try:
            idx, cnt = q.popleft()
        except:
            break
        for i in range(1, v + 1):
            if idx == g:
                res = cnt
                break
            elif arr[idx][i] == 1 and visit[i] == 0:
                q.append((i, cnt + 1))
                visit[i] = 1
        if res != 0:
            break
T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    arr = [[0] * (v + 1) for _ in range(v + 1)]
    visit = [0] * (v + 1)
    for i in range(e):
        y, x = map(int, input().split())
        arr[y][x] = 1
        arr[x][y] = 1
    s, g = map(int, input().split())
    visit[s] = 1
    cnt = 0
    res = 0
    bfs(s)
    print(f'#{test_case} {res}')