T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    ans = 0
    MIN = 21e8
    for i in range(n - 2):
        if lst[i] == lst[i+1]:
            continue
        for j in range(i + 1, n - 1):
            if lst[j] == lst[j + 1]:
                continue
            a = i + 1
            b = j - i
            c = n - a - b
            if a <= n // 2 and b <= n // 2 and c <= n // 2:
                ans = max(a, b, c) - min(a, b, c)
                MIN = min(ans, MIN)
    if MIN == 21e8:
        MIN = -1
    print(f'#{test_case} {MIN}')