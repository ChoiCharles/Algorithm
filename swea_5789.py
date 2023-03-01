import sys
sys.stdin = open('swea_5789_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n, q = map(int, input().split())
    lst = [0] * n
    for i in range(1, q + 1):
        l, r = map(int, input().split())
        for j in range(l-1, r):
            lst[j] = i
    print(f'#{test_case}', *lst)