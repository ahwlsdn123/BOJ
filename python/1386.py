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
    if u > v:
        parent[u] = v
    else:
        parent[v] = u

n = int(input())
edges = []
parent = [i for i in range(n)]
for i in range(n):
    edges.append([i,i,int(input())])
water = [False]*n
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(i+1,n):
        edges.append([i,j,tmp[j]])
edges.sort(key=lambda x:x[2])
answer = 0
for e in edges:
    a,b,c = e
    if water[find(a)] and water[find(b)]:
        continue
    if a == b:
        water[find(a)] = True
        answer += c
        continue
    if find(a) != find(b):
        water[find(a)] = water[find(b)] = water[find(a)] or water[find(b)]
        union(a,b)
        answer += c
print(answer)