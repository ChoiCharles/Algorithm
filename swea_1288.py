import sys
sys.stdin = open('swea_1288_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    i = 1
    lst = []
    while len(lst) < 10:
        a = list(str(n * i))
        for j in a:
            if j not in lst:
                lst.append(j)
        i += 1
    print(f'#{test_case} {n * (i - 1)}')