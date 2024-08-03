import sys
from collections import deque
from math import log2
input = sys.stdin.readline

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(u,v):
    u = find(u)
    v = find(v)
    if u > v:
        parent[u] = v
    else:
        parent[v] = u

n,m = map(int,input().split())
edges = []
for _ in range(m):
    edges.append(list(map(int,input().split())))
edges.sort(key=lambda x:x[2])
answer = 0
cnt = 0
parent = [i for i in range(n+1)]
neighbors = [[] for _ in range(n+1)]
for a,b,c in edges:
    if find(a) != find(b):
        union(a,b)
        answer += c
        cnt += 1
        neighbors[a].append([b,c])
        neighbors[b].append([a,c])
        if cnt == n-1:
            break
visited = [False]*(n+1)
visited[1] = True
depth = [0]*(n+1)
parent = [[0,0] for _ in range(n+1)]
q = deque([1])
while q:
    now = q.popleft()
    for x,c in neighbors[now]:
        if not visited[x]:
            visited[x] = True
            depth[x] = depth[now]+1
            parent[x] = [now,c]
            q.append(x)
logN = int(log2(n)+1)
dp = [[[0,0] for _ in range(logN)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = parent[i]
for j in range(1,logN):
    for i in range(n+1):
        dp[i][j][1] = max(dp[i][j-1][1],dp[dp[i][j-1][0]][j-1][1])
        dp[i][j][0] = dp[dp[i][j-1][0]][j-1][0]
q = int(input())
for d in range(q):
    x,y = map(int,input().split())
    if depth[x] > depth[y]:
        x,y = y,x
    diff = depth[y]-depth[x]
    dist_max = 0
    for i in range(logN-1,-1,-1):
        if diff & 1<<i:
            dist_max = max(dist_max,dp[y][i][1])
            y = dp[y][i][0]
    if x==y:
        print(answer-dist_max)
        continue
    for i in range(logN-1,-1,-1):
        if dp[x][i][0] != dp[y][i][0]:
            dist_max = max(dist_max,dp[x][i][1],dp[y][i][1])
            x = dp[x][i][0]
            y = dp[y][i][0]
    dist_max = max(dist_max,dp[x][0][1],dp[y][0][1])
    print(answer-dist_max)