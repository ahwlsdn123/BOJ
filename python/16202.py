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

n,m,k = map(int,input().split())
edges = []
for c in range(1,m+1):
    a,b = map(int,input().split())
    edges.append([a,b,c])
answer = []
for _ in range(k):
    parent = [i for i in range(n+1)]
    tmp = []
    w = 0
    for e in edges:
        a,b,c = e
        if find(a) != find(b):
            union(a,b)
            w += c
            tmp.append(e)
    if len(tmp) == n-1:
        answer.append(w)
    else:
        answer.append(0)
    edges.remove(tmp[0])
print(*answer)