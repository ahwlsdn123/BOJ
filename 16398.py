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
    if u < v:
        parent[v] = u
    else:
        parent[u] = v

n = int(input())
parent = [i for i in range(n)]
edges = []
for i in range(n):
    cost = list(map(int, input().split()))
    for j in range(i+1,n):
        edges.append([i,j,cost[j]])
edges.sort(key=lambda x:x[2])
answer = 0
for e in edges:
    a,b,c = e
    if find(a) != find(b):
        union(a,b)
        answer += c
print(answer)