import sys
sys.stdin = open("swea_1926_input.txt", "r")

T = int(input())
result = []
for i in range(1, T + 1):
    a = str(i)
    lst = list(a)
    k = 0
    for j in lst:
        if int(j) % 3 == 0 and int(j) != 0:
            k += 1
    if k == 3:
        result.append('---')
    elif k == 2:
        result.append('--')
    elif k == 1:
        result.append('-')
    else:
        result.append(i)

print(*result)