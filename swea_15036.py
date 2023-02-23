import sys
sys.stdin = open('swea_15036_input.txt', 'r')

def asdf(n, g):
    global flag
    if flag > 0:
        return
    if n == g:
        flag += 1
        return
    for i in range(len(arr)):
        if arr[n][i] == 1 and visit[i] == 0:
            visit[i] = 1
            asdf(i, g)
            visit[i] = 0

T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    arr = [[0]*(v+1) for _ in range(v+1)]
    visit = [0] * (v+1)
    for i in range(e):
        y, x = map(int, input().split())
        arr[y-1][x-1] = 1
    s, g = map(int, input().split())
    flag = 0
    visit[s-1] = 1
    asdf(s-1, g-1)
    if flag > 0:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')