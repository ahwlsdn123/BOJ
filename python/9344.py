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

t = int(input())
for _ in range(t):
    n,m,p,q = map(int,input().split())
    parent = [i for i in range(n+1)]
    edges = []
    for _ in range(m):
        edges.append(list(map(int,input().split())))
    edges.sort(key=lambda x:x[2])
    did = False
    for a,b,c in edges:
        if find(a) != find(b):
            union(a,b)
            if (a==p and b==q) or (a==q and b==p):
                print('YES')
                did = True
                break
    if not did:
        print('NO')