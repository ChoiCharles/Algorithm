T = int(input())
for test_case in range(1, T + 1):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    x = x2 - x1
    y = y2 - y1
    R = (x**2 + y**2)**0.5
    r = r1 + r2
    if r1 > r2:
        RR = r1
        rr = r2
    else:
        RR = r2
        rr = r1
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif x1 == x2 and y1 == y2 and r1 != r2:
        print(0)
    elif R + rr < RR:
        print(0)
    elif R + rr == RR:
        print(1)
    elif R == r:
        print(1)
    elif R < r:
        print(2)
    elif R > r:
        print(0)