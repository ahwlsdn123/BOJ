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
    s,p = map(int,input().split())
    coords = []
    for _ in range(p):
        coords.append(list(map(int,input().split())))
    edges = []
    for i in range(p):
        for j in range(i+1,p):
            edges.append([i,j,((coords[i][0]-coords[j][0])**2+(coords[i][1]-coords[j][1])**2)**0.5])
    edges.sort(key=lambda x:x[2])
    cnt = 0
    parent = [i for i in range(p)]
    for a,b,c in edges:
        if find(a) != find(b):
            union(a,b)
            cnt += 1
            if cnt == p-s:
                print('{:.2f}'.format(c))
                break