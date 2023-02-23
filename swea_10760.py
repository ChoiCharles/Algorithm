import sys
sys.stdin = open("swea_10760_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dx = [1, 0, -1, 0, 1, -1, -1, 1]
    dy = [0, 1, 0, -1, 1, 1, -1, -1]
    result = 0
    for i in range(n):
        for j in range(m):
            cnt = 0
            for k in range(8):
                if 0 <= i+dy[k] < n and 0 <= j+dx[k] < m:
                    if arr[i][j] > arr[i+dy[k]][j+dx[k]]:
                        cnt += 1
            if cnt > 3:
                result += 1
    print(f'#{test_case} {result}')