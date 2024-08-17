import sys
from math import log2
from collections import deque
input = sys.stdin.readline

INF = 5000000000

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

v,e = map(int,input().split())
edges = []
for _ in range(e):
    a,b,c = list(map(int,input().split()))
    if a==b: continue
    edges.append([a,b,c])
edges.sort(key=lambda x:x[2])
parent = [i for i in range(v+1)]
mst = [[] for i in range(v+1)]
trash = []
cnt = 0
weight_sum = 0
for i in range(len(edges)):
    a,b,c = edges[i]
    if find(a) != find(b):
        union(a,b)
        mst[a].append([b,c])
        mst[b].append([a,c])
        weight_sum += c
        cnt += 1
        if cnt == v-1:
            trash.extend(edges[i+1:])
            break
    else:
        trash.append([a,b,c])
if cnt < v-1 or not trash:
    print(-1)
else:
    answer = INF
    parent = [[0,0]]*(v+1)
    depth = [0]*(v+1)
    visited = [False]*(v+1)
    visited[1] = True
    q = deque([1])
    while q:
        now = q.popleft()
        for x,c in mst[now]:
            if not visited[x]:
                parent[x] = [now,c]
                depth[x] = depth[now]+1
                visited[x] = True
                q.append(x)
    logV = int(log2(v)+1)
    dp = [[[0,-1,-1] for _ in range(logV)] for _ in range(v+1)]
    for i in range(v+1):
        dp[i][0][:2] = parent[i]
    for j in range(1,logV):
        for i in range(v+1):
            pq = []
            tmp1 = dp[i][j-1]
            tmp2 = dp[tmp1[0]][j-1]
            pq.append(tmp1[1])
            pq.append(tmp1[2])
            pq.append(tmp2[1])
            pq.append(tmp2[2])
            pq.sort(reverse=True)
            dp[i][j][1] = pq[0]
            for l in range(1,4):
                if pq[l] < pq[0]:
                    dp[i][j][2] = pq[l]
                    break
            dp[i][j][0] = tmp2[0]
    for a,b,c in trash:
        if depth[a] > depth[b]:
            a,b = b,a
        diff = depth[b]-depth[a]
        max_weight_to_lca = -1
        for i in range(logV):
            if diff & 1<<i:
                tmp = dp[b][i]
                if tmp[1] < c:
                    max_weight_to_lca = max(max_weight_to_lca,tmp[1])
                else:
                    max_weight_to_lca = max(max_weight_to_lca,tmp[2])
                b = tmp[0]
        if a == b:
            if max_weight_to_lca != -1:
                answer = min(answer,weight_sum-max_weight_to_lca+c)
            continue
        for i in range(logV-1,-1,-1):
            if dp[a][i][0] != dp[b][i][0]:
                tmp1,tmp2 = dp[a][i],dp[b][i]
                if tmp1[1] < c:
                    max_weight_to_lca = max(max_weight_to_lca,tmp1[1])
                else:
                    max_weight_to_lca = max(max_weight_to_lca,tmp1[2])
                if tmp2[1] < c:
                    max_weight_to_lca = max(max_weight_to_lca,tmp2[1])
                else:
                    max_weight_to_lca = max(max_weight_to_lca,tmp2[2])
                a = tmp1[0]
                b = tmp2[0]
        tmp1,tmp2 = dp[a][0],dp[b][0]
        if tmp1[1] < c:
            max_weight_to_lca = max(max_weight_to_lca,tmp1[1])
        else:
            max_weight_to_lca = max(max_weight_to_lca,tmp1[2])
        if tmp2[1] < c:
            max_weight_to_lca = max(max_weight_to_lca,tmp2[1])
        else:
            max_weight_to_lca = max(max_weight_to_lca,tmp2[2])
        if max_weight_to_lca != -1:
            answer = min(answer,weight_sum-max_weight_to_lca+c)
    if answer != INF:
        print(answer)
    else:
        print(-1)