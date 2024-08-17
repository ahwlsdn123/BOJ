import sys
input = sys.stdin.readline

def find(v):
    global parent
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(u,v):
    global parent
    u = find(u)
    v = find(v)
    if u > v:
        parent[u] = v
    else:
        parent[v] = u

n,m = map(int, input().split())
edges = []
parent = [i for i in range(n+1)]
answer = 0
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append([a,b,c])
    answer += c
edges.sort(key=lambda x:x[2])
cnt = 0
for e in edges:
    a,b,c = e
    if find(a) != find(b):
        union(a,b)
        answer -= c
        cnt += 1
if cnt == n-1:
    print(answer)
else:
    print(-1)