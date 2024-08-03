import sys
input = sys.stdin.readline
from math import log2
from collections import deque

def lca(u,v):
    global depth, logN, dp
    if depth[u] > depth[v]:
        u,v = v,u
    diff = depth[v]-depth[u]
    for i in range(logN):
        if diff & 1<<i:
            v = dp[v][i]
    if u == v:
        return u
    for i in range(logN-1,-1,-1):
        if dp[u][i] != dp[v][i]:
            u = dp[u][i]
            v = dp[v][i]
    return dp[u][0]

n = int(input())
tree = [[] for _ in range(n+1)]
parent = [0]*(n+1)
visited = [False]*(n+1)
depth = [0]*(n+1)
for _ in range(n-1):
    u,v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
q = deque([1])
visited[1] = True
while q:
    x = q.popleft()
    for child in tree[x]:
        if not visited[child]:
            visited[child] = True
            parent[child] = x
            depth[child] = depth[x]+1
            q.append(child)
logN = int(log2(n)+1)
dp = [[0 for _ in range(logN)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = parent[i]
for j in range(1,logN):
    for i in range(n+1):
        dp[i][j] = dp[dp[i][j-1]][j-1]
m = int(input())
for _ in range(m):
    r,u,v = map(int, input().split())
    a1 = lca(u,v)
    a2 = lca(r,u)
    a3 = lca(r,v)
    if a2 == a3:
        print(a1)
    elif a1 == a3:
        print(a2)
    else:
        print(a3)