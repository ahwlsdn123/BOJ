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
parent = [i for i in range(n)]
cost = 0
edges = []
for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(i+1,n):
        if arr[j] < 0:
            union(i,j)
            cost -= arr[j]
        else:
            edges.append([i,j,arr[j]])
cnt = 0
new_roads = []
edges.sort(key=lambda x:x[2])
for a,b,c in edges:
    if find(a) != find(b):
        union(a,b)
        cost += c
        cnt += 1
        new_roads.append([a+1,b+1])
print(cost,cnt)
for i,j in new_roads:
    print(i,j)