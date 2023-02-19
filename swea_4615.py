import sys
sys.stdin = open('swea_4615_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+2) for _ in range(N+2)]
    m = N//2
    arr[m][m] = arr[m+1][m+1] = 2
    arr[m][m+1] = arr[m+1][m] = 1
    for i in range(M):
        si, sj, c = map(int, input().split())
        arr[si][sj] = c
        for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
            tlst = []
            for j in range(1, N):
                if arr[si+di*j][sj+dj*j] == 0:
                    break
                elif arr[si+di*j][sj+dj*j] != c:
                    tlst.append((si+di*j, sj+dj*j))
                else:
                    while tlst:
                        ni, nj = tlst.pop()
                        arr[ni][nj] = c
                    break
    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f'#{test_case} {bcnt} {wcnt}')