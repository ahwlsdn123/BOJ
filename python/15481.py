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
for i in range(m):
    a,b,c = map(int,input().split())
    edges.append([a,b,c,i])
edges.sort(key=lambda x:x[2])
answer = [0]*m
parent = [i for i in range(n+1)]
val = 0
cnt = 0
indices = []
tmp = []
roads = [[] for _ in range(n+1)]
for a,b,c,d in edges:
    if find(a) != find(b):
        union(a,b)
        val += c
        cnt += 1
        indices.append(d)
        tmp.append([a,b,c,d])
        roads[a].append([b,c,d])
        roads[b].append([a,c,d])
        if cnt == n-1:
            break
for i in indices:
    answer[i] = val
parent = [[0,0,0] for _ in range(n+1)]
depth = [0]*(n+1)
visited = [False]*(n+1)
q = deque([1])
visited[1] = True
while q:
    now = q.popleft()
    for x,c,d in roads[now]:
        if not visited[x]:
            visited[x] = True
            depth[x] = depth[now]+1
            parent[x] = [now,c,d]
            q.append(x)
logN = int(log2(n)+1)
dp = [[[0,0,0] for _ in range(logN)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = parent[i]
for j in range(1,logN):
    for i in range(n+1):
        dp[i][j][0] = dp[dp[i][j-1][0]][j-1][0]
        a = dp[dp[i][j-1][0]][j-1]
        b = dp[i][j-1]
        if a[1] > b[1]:
            dp[i][j][1] = a[1]
            dp[i][j][2] = a[2]
        else:
            dp[i][j][1] = b[1]
            dp[i][j][2] = b[2]
edges.sort(key=lambda x:x[3])
for j in range(m):
    if answer[j] != 0:
        continue
    a,b,c,_ = edges[j]
    if depth[a]>depth[b]:
        a,b=b,a
    diff = depth[b]-depth[a]
    max_val = 0
    index_edge = 0
    for i in range(logN):
        if diff & 1<<i:
            tmp1 = dp[b][i]
            if max_val < tmp1[1]:
                max_val = tmp1[1]
                index_edge = tmp1[2]
            b = tmp1[0]
    if a != b:
        for i in range(logN-1,-1,-1):
            tmp1 = dp[a][i]
            tmp2 = dp[b][i]
            if tmp1[0] != tmp2[0]:
                if max_val < tmp1[1]:
                    max_val = tmp1[1]
                    index_edge = tmp1[2]
                if max_val < tmp2[1]:
                    max_val = tmp2[1]
                    index_edge = tmp2[2]
                a = tmp1[0]
                b = tmp2[0]
        tmp1 = dp[a][0]
        tmp2 = dp[b][0]
        if max_val < tmp1[1]:
            max_val = tmp1[1]
            index_edge = tmp1[2]
        if max_val < tmp2[1]:
            max_val = tmp2[1]
            index_edge = tmp2[2]
    answer[j] = val-max_val+c
for a in answer:
    print(a)