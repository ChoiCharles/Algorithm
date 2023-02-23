import sys
sys.stdin = open("swea_13685_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    st = input()
    cnt = 0
    result = 0
    for i in range(len(st)):
        if st[i] == '(':
            cnt += 1
        else:
            if st[i-1] == '(':
                cnt -= 1
                result += cnt
            else:
                cnt -= 1
                result += 1
    print(f'#{test_case} {result}')