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
m = int(input())
parent = [i for i in range(n+1)]
edges = []
for _ in range(m):
    a,b,c = map(int, input().split())
    if a == b:
        continue
    edges.append([a,b,c])
edges.sort(key=lambda x:x[2])
answer = 0
for e in edges:
    a,b,c = e
    if find(a) != find(b):
        union(a,b)
        answer += c
print(answer)