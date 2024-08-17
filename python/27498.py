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

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
edges = []
answer = 0
cnt = 0
for _ in range(m):
    a,b,c,d = map(int,input().split())
    if d == 1:
        union(a,b)
        cnt += 1
    else:
        edges.append([a,b,c])
        answer += c
if cnt == n-1:
    print(answer)
    sys.exit(0)
edges.sort(key=lambda x:-x[2])
for a,b,c in edges:
    if find(a) != find(b):
        union(a,b)
        answer -= c
        cnt += 1
        if cnt == n-1:
            print(answer)
            break