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

def dfs(cur,prev):
    answer.append([prev,cur])
    visited[cur] = True
    for v in neighbors[cur]:
        if not visited[v]:
            dfs(v,cur)

n = int(input())
p = [0]
c = [0]
for _ in range(n):
    a,b = map(int,input().split())
    p.append(a)
    c.append(b)
edges = []
for i in range(1,n+1):
    for j in range(i+1,n+1):
        edges.append([i,j,int((c[i]+c[j])/abs(p[i]-p[j]))])
edges.sort(key=lambda x:-x[2])
sum_watch = 0
neighbors = [[] for _ in range(n+1)]
parent = [i for i in range(n+1)]
for c1,c2,watch in edges:
    if find(c1) != find(c2):
        union(c1,c2)
        sum_watch += watch
        neighbors[c1].append(c2)
        neighbors[c2].append(c1)
visited = [False]*(n+1)
answer = []
dfs(1,0)
print(sum_watch)
for i in range(n-1,0,-1):
    print(*answer[i])