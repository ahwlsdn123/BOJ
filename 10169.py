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
answer = [-1]*m
roads = []
for i in range(m):
    roads.append(list(map(int,input().split()))+[i])
sorted_roads = roads.copy()
sorted_roads.sort(key=lambda x:x[2])
cnt = 0
parent = [i for i in range(n+1)]
min_dist = 0
selected_roads = []
not_selected_roads = []
neightbors = [[] for _ in range(n+1)]
for i in range(m):
    a,b,c,d = sorted_roads[i]
    if find(a) != find(b):
        union(a,b)
        cnt += 1
        min_dist += c
        selected_roads.append(d)
        neightbors[a].append([b,d])
        neightbors[b].append([a,d])
        if cnt == n-1:
            for j in range(i+1,m):
                not_selected_roads.append(sorted_roads[j][3])
            break
    else:
        not_selected_roads.append(d)
if cnt < n-1:
    for _ in range(m):
        print(-1)
    sys.exit(0)
for i in not_selected_roads:
    answer[i] = min_dist
visited = [False]*(n+1)
parent = [[0,0] for _ in range(n+1)]
depth = [0]*(n+1)
q = deque([1])
visited[1] = True
while q:
    now = q.popleft()
    for x,r in neightbors[now]:
        if not visited[x]:
            visited[x] = True
            parent[x] = [now,r]
            depth[x] = depth[now]+1
            q.append(x)
logN = int(log2(n)+1)
dp = [[0 for _ in range(logN)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = parent[i][0]
for j in range(1,logN):
    for i in range(n+1):
        dp[i][j] = dp[dp[i][j-1]][j-1]
for i in not_selected_roads:
    a,b,c,_ = roads[i]
    lca = 0
    if depth[a] > depth[b]:
        a,b = b,a
    diff = depth[b]-depth[a]
    for j in range(logN):
        if diff & 1<<j:
            b = dp[b][j]
    if a==b:
        lca = a
    else:
        for j in range(logN-1,-1,-1):
            if dp[a][j] != dp[b][j]:
                a = dp[a][j]
                b = dp[b][j]
        lca = dp[a][0]
    a,b = roads[i][:2]
    while a != lca:
        p,r = parent[a]
        if answer[r] == -1:
            answer[r] = min_dist-roads[r][2]+c
        else:
            answer[r] = min(answer[r],min_dist-roads[r][2]+c)
        a = p
    while b != lca:
        p,r = parent[b]
        if answer[r] == -1:
            answer[r] = min_dist-roads[r][2]+c
        else:
            answer[r] = min(answer[r],min_dist-roads[r][2]+c)
        b = p
print(*answer,sep='\n')