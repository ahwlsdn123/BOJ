import sys
input = sys.stdin.readline

from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    in_degree = [0]*(n+1)
    outs = [set() for _ in range(n+1)]
    for i in range(n):
        in_degree[arr[i]] = i
        outs[arr[i]] = set(arr[i+1:n])
    m = int(input())
    for _ in range(m):
        a,b = map(int, input().split())
        if a in outs[b]:
            outs[b].discard(a)
            outs[a].add(b)
            in_degree[a] -= 1
            in_degree[b] += 1
        else:
            outs[a].discard(b)
            outs[b].add(a)
            in_degree[b] -= 1
            in_degree[a] += 1
    queue = deque()
    for i in range(1,n+1):
        if in_degree[i] == 0:
            queue.append(i)
    uncertain = False
    answer = []
    while queue:
        x = queue.popleft()
        if len(queue) != 0:
            uncertain = True
            break
        answer.append(x)
        for o in outs[x]:
            in_degree[o] -= 1
            if in_degree[o] == 0:
                queue.append(o)
    if uncertain:
        print('?')
    elif len(answer) != n:
        print('IMPOSSIBLE')
    else:
        print(*answer)