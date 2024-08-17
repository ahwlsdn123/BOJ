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

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    union(a,b)
input()
edges = []
for i in range(2,n+1):
    arr = list(map(int,input().split()))
    for j in range(i+1,n+1):
        heapq.heappush(edges,[arr[j-1],i,j])
answer = 0
tmp = []
while edges:
    c,a,b = heapq.heappop(edges)
    if find(a) != find(b):
        union(a,b)
        tmp.append([a,b])
        answer += c
print(answer, len(tmp))
for el in tmp:
    print(*el)