import sys
sys.stdin = open("swea_1953_input.txt", "r")

from collections import deque
type1 = ((-1, 0), (1, 0), (0, -1), (0, 1))
type2 = ((-1, 0), (1, 0))
type3 = ((0, -1), (0, 1))
type4 = ((-1, 0), (0, 1))
type5 = ((1, 0), (0, 1))
type6 = ((1, 0), (0, -1))
type7 = ((-1, 0), (0, -1))
pipe = [0, type1, type2, type3, type4, type5, type6, type7]
def asdf(y, x):
    q = deque()
    t = deque()
    q.append((y, x))
    visit[y][x] = 1
    t.append(1)
    cnt = 1
    while 1:
        try:
            time = t.pop()
        except:
            return cnt
        if time > l:
            cnt -= 1
            continue
        y, x = q.popleft()
        p = arr[y][x]
        for di, dj in pipe[p]:
            if 0 <= y + di < n and 0 <= x + dj < m:
                if arr[y + di][x + dj] != 0 and visit[y + di][x + dj] == 0:
                    for ni, nj in pipe[arr[y + di][x + dj]]:
                        if di + ni == 0 and dj + nj == 0:
                            cnt += 1
                            visit[y + di][x + dj] = visit[y][x] + 1
                            q.append((y + di, x + dj))
                            t.append(visit[y + di][x + dj])
T = int(input())
for test_case in range(1, T + 1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0]*m for _ in range(n)]
    res = asdf(r, c)
    print(f'#{test_case} {res}')