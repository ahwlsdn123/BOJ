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
        parent[u] = v
    else:
        parent[v] = u

n,m,k = map(int, input().split())
parent = [i for i in range(n+1)]
charged = [False]*(n+1)
ks = list(map(int, input().split()))
for a in ks:
    charged[a] = True
edges = []
for _ in range(m):
    u,v,w = map(int, input().split())
    edges.append([u,v,w])
edges.sort(key=lambda x:x[2])
answer = 0
for e in edges:
    u,v,w = e
    charged[u] = charged[find(u)]
    charged[v] = charged[find(v)]
    if charged[u] and charged[v]:
        continue
    if find(u) != find(v):
        union(u,v)
        charged[find(u)] = charged[u] = charged[v] = charged[u] or charged[v]
        answer += w
print(answer)