from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
in_degree = [0 for _ in range(n+1)]
outs = [[] for _ in range(n+1)]
queue = deque()
answer = []

for _ in range(m):
    f,t = map(int, input().split())
    in_degree[t] += 1
    outs[f].append(t)

for i in range(1,n+1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()
    answer.append(x)
    for o in outs[x]:
        in_degree[o] -= 1
        if in_degree[o] == 0:
            queue.append(o)

print(*answer)