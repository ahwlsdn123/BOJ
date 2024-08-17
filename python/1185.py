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

n,p = map(int,input().split())
point_cost = [0] + [int(input()) for _ in range(n)]
edges = []
for _ in range(p):
    s,e,l = map(int,input().split())
    heapq.heappush(edges,[2*l+point_cost[s]+point_cost[e],s,e])
parent = [i for i in range(n+1)]
answer = min(point_cost[1:])
tmp = []
while edges:
    c,s,e = heapq.heappop(edges)
    if find(s) != find(e):
        union(s,e)
        answer += c
        tmp.append([c,s,e])
print(answer)