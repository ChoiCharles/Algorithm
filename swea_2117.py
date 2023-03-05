import sys
sys.stdin = open("swea_2117_input.txt", "r")

cost = [k*k+(k-1)*(k-1) for k in range(40)]

# def asdf():
#     home = []
#     mx = 0
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == 1:
#                 home.append((i, j))
#     for i in range(n):
#         for j in range(n):
#             dist = [0] * 40
#             for hi, hj in home:
#                 a = abs(i-hi) + abs(j-hj) + 1
#                 dist[a] += 1
#             for k in range(1, 40):
#                 dist[k] += dist[k - 1]
#                 if cost[k] <= dist[k] * m:
#                     mx = max(mx, dist[k])
#     return mx

def bfs(y, x):
    q = []
    q.append((y, x))
    v = [[0] * n for _ in range(n)]
    v[y][x] = 1
    flag = 0
    cnt = 0
    cnt += arr[y][x]
    mx = 0
    while q:
        ci, cj = q.pop(0)
        if flag != v[ci][cj]:
            flag = v[ci][cj]
            if cost[flag] <= cnt * m:
                mx = max(mx, cnt)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and v[ni][nj] == 0:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))
                cnt += arr[ni][nj]
    return mx

def asdf():
    mx = 0
    for i in range(n):
        for j in range(n):
            mx = max(mx, bfs(i, j))
    return mx

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = asdf()
    print(f'#{test_case} {ans}')