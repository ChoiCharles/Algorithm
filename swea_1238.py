import sys
sys.stdin = open('swea_1238_input.txt', 'r')

from collections import deque

def bfs(a):
    global n, t
    q = deque()
    visit = [0] * (101)
    q.append(a)
    visit[a] = 1
    time[a] = t
    res = [(t, a)]
    while q:
        node = q.popleft()
        for i in arr[node]:
            if visit[i] == 0:
                time[i] = time[node] + 1
                q.append(i)
                visit[i] = 1
                res.append((time[i], i))
    return res

T = 10
for test_case in range(1, T + 1):
    n, s = map(int, input().split())
    arr = [[] for _ in range(101)]
    lst = list(map(int, input().split()))
    time = [0] * (101)
    while lst:
        a = lst.pop(0)
        b = lst.pop(0)
        arr[a].append(b)
    t = 1
    r = bfs(s)
    res = sorted(r, key = lambda x:(x[0], x[1]))
    print(f'#{test_case} {res[-1][-1]}')