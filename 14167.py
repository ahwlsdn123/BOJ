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

n = int(input())
coords = []
for _ in range(n):
    coords.append(list(map(int,input().split())))
edges = []
for i in range(n):
    for j in range(i+1,n):
        edges.append([i,j,(coords[i][0]-coords[j][0])**2+(coords[i][1]-coords[j][1])**2])
edges.sort(key=lambda x:x[2])
cnt = 0
parent = [i for i in range(n)]
for a,b,c in edges:
    if find(a) != find(b):
        union(a,b)
        cnt += 1
        if cnt == n-1:
            print(c)
            sys.exit(0)