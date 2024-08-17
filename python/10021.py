import sys
import heapq
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
    if u > v:
        parent[u] = v
    else:
        parent[v] = u

n,c = map(int,input().split())
coords = []
for _ in range(n):
    coords.append(list(map(int,input().split())))
edges = []
for i in range(n):
    for j in range(i+1,n):
        val = (coords[i][0]-coords[j][0])**2+(coords[i][1]-coords[j][1])**2
        if val >= c:
            heapq.heappush(edges,[val,i,j])
parent = [i for i in range(n)]
answer = 0
cnt = 0
for e in edges:
    c,a,b = e
    if find(a) != find(b):
        union(a,b)
        answer += c
        cnt += 1
        if cnt == n-1:
            break
if cnt == n-1:
    print(answer)
else:
    print(-1)