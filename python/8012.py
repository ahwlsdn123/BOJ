import sys
from collections import deque
from math import log2
input = sys.stdin.readline

n = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
visited = [False]*(n+1)
depth = [0]*(n+1)
parent = [0]*(n+1)
q = deque([1])
visited[1] = True
while q:
    now = q.popleft()
    for x in edges[now]:
        if not visited[x]:
            visited[x] = True
            depth[x] = depth[now]+1
            parent[x] = now
            q.append(x)
logN = int(log2(n)+1)
dp = [[0 for _ in range(logN)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = parent[i]
for j in range(1,logN):
    for i in range(n+1):
        dp[i][j] = dp[dp[i][j-1]][j-1]
m = int(input())
prev = 1
answer = 0
for _ in range(m):
    now = int(input())
    u,v = prev,now
    if depth[u] > depth[v]:
        u,v = v,u
    diff = depth[v]-depth[u]
    for i in range(logN):
        if diff & 1<<i:
            v = dp[v][i]
    answer += diff
    prev = now
    if u == v:
        continue
    for i in range(logN-1,-1,-1):
        if dp[u][i] != dp[v][i]:
            u = dp[u][i]
            v = dp[v][i]
            answer += 1<<(i+1)
    answer += 2
print(answer)