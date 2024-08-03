import sys
import heapq
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
edges = []
for i in range(1,n):
    arr = list(map(int,input().split()))
    for j in range(i+1,n+1):
        heapq.heappush(edges,[arr[j-i-1],i,j])
parent = [i for i in range(n+1)]
adj = [[] for _ in range(n+1)]
while edges:
    c,a,b = heapq.heappop(edges)
    if find(a) != find(b):
        union(a,b)
        adj[a].append(b)
        adj[b].append(a)
for i in range(1,n+1):
    print(len(adj[i]),*sorted(adj[i]))