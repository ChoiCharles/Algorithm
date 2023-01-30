# SW Expert Academy_1859

import sys
sys.stdin = open("swea_1859_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    a = lst[-1]
    rev = 0
    for i in range(len(lst) - 1, -1, -1):
        if a < lst[i]:
            a = lst[i]
        elif a > lst[i]:
            rev += (a - lst[i])
    print(f'#{test_case} {rev}')