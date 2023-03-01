import sys
sys.stdin = open('swea_4613_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    MIN = int(21e8)
    i = 1       # 흰색으로 칠할 부분 까지의 인덱스
    j = i + 1   # 파란색으로 칠할 부분 까지의 인덱스

    while 1:
        cnt = 0
        # count를 이용해 탐색
        for l in range(i):
            cnt += arr[l].count('B')
            cnt += arr[l].count('R')
        for l in range(i, j):
            cnt += arr[l].count('W')
            cnt += arr[l].count('R')
        for l in range(j, n):
            cnt += arr[l].count('W')
            cnt += arr[l].count('B')
        MIN = min(MIN, cnt)
        # i(흰색)의 값이 n - 2 여야 파란색과 빨간색이 최소한으로 있으므로 반복문 탈출
        if i == n - 2:
            break
        # 현재 i(흰색)값에서 파란색이 최대 많이 칠해지려면 j = n - 1이어야함
        # j = n - 1이 되면 흰색(i)을 한칸 더 칠해 다음 탐색으로 넘어가고 j를 i - 1로 초기화
        elif j == n - 1:
            i += 1
            j = i + 1
        # 그 외에는 파란 부분을 한칸씩 늘려서 탐색
        else:
            j += 1
    print(f'#{test_case} {MIN}')