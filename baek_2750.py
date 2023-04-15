import sys
input = sys.stdin.readline


n = int(input())
lst = []
for i in range(n):
    a = int(input())
    lst.append(a)
for i in range(n-1):
    for j in range(n-1-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
for i in lst:
    print(i)