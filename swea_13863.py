import sys
sys.stdin = open("swea_13863_input.txt", "r")

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def asdf(y, x):
    global flag, n
    if flag > 0:
        return
    for i in range(4):
        if 0 <= y+dy[i] < n and 0 <= x+dx[i] < n:
            if arr[y+dy[i]][x+dx[i]] == '0':
                arr[y][x] = '1'
                asdf(y+dy[i], x+dx[i])
                arr[y][x] = '0'
            elif arr[y+dy[i]][x+dx[i]] == '3':
                flag += 1
                return

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                y = i
                x = j
    flag = 0
    asdf(y, x)
    if flag > 0:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')