# SW Expert Academy-2007

import sys
sys.stdin = open("swea_2007_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    st = list(input())
    a = st[0]
    for i in range(1, len(st)):
        if a == st[i]:
            if st[:i] == st[i:i*2]:
                result = len(st[:i])
                break
            else:
                continue
    print(f'#{test_case} {result}')