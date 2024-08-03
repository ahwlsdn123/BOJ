import sys
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

def dfs(v):
    visited[v] = True
    r1 = r2 = r3 = 0
    for n,c in neighbors[v]:
        if not visited[n]:
            tmp1,tmp2 = dfs(n)
            if r1 < tmp1+c:
                r2 = r1
                r1 = tmp1+c
            elif r2 < tmp1+c:
                r2 = tmp1+c
            r3 = max(r3,tmp2)
    return r1, max(r1+r2,r3)

n,k = map(int,input().split())
edges = []
for _ in range(k):
    edges.append(list(map(int,input().split())))
edges.sort(key=lambda x:x[2])
parent = [i for i in range(n)]
answer = 0
cnt = 0
neighbors = [[] for _ in range(n)]
for a,b,c in edges:
    if find(a) != find(b):
        union(a,b)
        answer += c
        cnt += 1
        neighbors[a].append([b,c])
        neighbors[b].append([a,c])
        if cnt == -1:
            break
print(answer)
visited = [False]*n
print(dfs(0)[1])