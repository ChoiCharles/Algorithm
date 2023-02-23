import sys
sys.stdin = open('swea_1231_input.txt', 'r')

def inorder(a):
    if a > len(tree) - 1:
        return
    inorder(a * 2)
    print(tree[a], end = '')
    inorder(a * 2 + 1)
T = 10
for test_case in range(1, T + 1):
    n = int(input())
    tree = [0] * (n + 1)
    for i in range(n):
        a = list(input().split())
        idx = int(a[0])
        tree[idx] = a[1]
    print(f'#{test_case}', end = ' ')
    inorder(1)
    print()