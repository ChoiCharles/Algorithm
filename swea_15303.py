import sys
sys.stdin = open("swea_15303_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, m, l = map(int, input().split())
    tree = [0] * (n + 1)
    for i in range(m):
        idx, num = map(int, input().split())
        tree[idx] = num
    for i in range(m, 0, -1):
        if tree[i] == 0:
            if i * 2 + 1 <= n:
                tree[i] = tree[i*2] + tree[i*2+1]
            else:
                tree[i] = tree[i*2]
    print(f'#{test_case} {tree[l]}')