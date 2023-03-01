import sys
sys.stdin = open('swea_4789_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input()))
    sum = 0
    cnt = 0
    for i in range(len(lst)):
        if sum < i:
            cnt += 1
            sum += lst[i] + 1
            continue
        sum += lst[i]
    print(f'#{test_case} {cnt}')