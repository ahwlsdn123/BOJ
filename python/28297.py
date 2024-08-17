import sys
from math import acos,pi,sqrt
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
gears = []
for _ in range(n):
    gears.append(list(map(int,input().split())))
edges = []
for i in range(n):
    for j in range(i+1,n):
        d_square = (gears[i][0]-gears[j][0])**2 + (gears[i][1]-gears[j][1])**2
        r1 = gears[i][2]
        r2 = gears[j][2]
        if d_square > (r1+r2)**2:
            d = sqrt(d_square)
            angle = 2*acos((r1-r2)/d)
            edges.append([i,j,r1*(2*pi-angle) + r2*angle + 2*sqrt(d_square-(r1-r2)**2)])
        else:
            edges.append([i,j,0])
edges.sort(key=lambda x:x[2])
cnt = 0
parent = [i for i in range(n)]
answer = 0
for a,b,c in edges:
    if find(a) != find(b):
        union(a,b)
        cnt += 1
        answer += c
        if cnt == n-1:
            break
print(answer)