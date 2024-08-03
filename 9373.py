import sys
import heapq
from math import sqrt
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
    w = int(input())
    n = int(input())
    if n == 0:
        print("{:.6f}".format(w/2))
        continue
    sensors = []
    for _ in range(n):
        sensors.append(list(map(int,input().split())))
    parent = [i for i in range(n+2)] # 0은 왼쪽 벽, 1은 오른쪽 벽
    edges = []
    for i in range(n):
        x,_,r = sensors[i]
        heapq.heappush(edges,[x-r,0,i+2])
        heapq.heappush(edges,[w-x-r,1,i+2])
    for i in range(n):
        for j in range(i+1,n):
            x1,y1,r1 = sensors[i]
            x2,y2,r2 = sensors[j]
            heapq.heappush(edges,[((x1-x2)**2+(y1-y2)**2)**0.5-r1-r2,i+2,j+2])
    while edges:
        c,a,b = heapq.heappop(edges)
        if find(a) != find(b):
            union(a,b)
            if find(0) == find(1):
                print("{:.6f}".format(max(0,c/2)))
                break