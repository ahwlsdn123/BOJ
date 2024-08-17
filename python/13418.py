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
    if u>v:
        parent[u]=v
    else:
        parent[v]=u

n,m = map(int, input().split())
edges = []
parent = [i for i in range(n+1)]
for _ in range(m+1):
    a,b,c = list(map(int, input().split()))
    edges.append([a,b,1-c])
edges.sort(key=lambda x:x[2])
k1 = 0
for e in edges:
    a,b,c = e
    if find(a) != find(b):
        union(a,b)
        k1 += c
edges.sort(key=lambda x:-x[2])
k2 = 0
parent = [i for i in range(n+1)]
for e in edges:
    a,b,c = e
    if find(a) != find(b):
        union(a,b)
        k2 += c
print(k2**2-k1**2)