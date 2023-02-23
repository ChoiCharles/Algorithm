import sys
sys.stdin = open("swea_13866_input.txt", "r")


def asdf(now):
    global MIN, cnt, n
    if cnt > MIN:
        return
    if now == n:
        MIN = cnt
        return
    for i in range(n):
        if visit[i] == 0:
            cnt += arr[now][i]
            visit[i] = 1
            asdf(now + 1)
            visit[i] = 0
            cnt -= arr[now][i]

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [0] * n
    MIN = 21e8
    cnt = 0
    asdf(0)
    print(f'#{test_case} {MIN}')