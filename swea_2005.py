# SW Expert Academy-2005

import sys
sys.stdin = open("swea_2005_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    result = [[1]]
    for i in range(n - 1):
        a = [1]
        for j in range(i):
            a += [result[i][j + 1] + result[i][j]]
        a += [1]
        result.append(a)
    print(f'#{test_case}')
    for i in result:
        print(*i)