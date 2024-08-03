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

n,m = map(int,input().split())
edges = []
for _ in range(m):
    edges.append(list(map(int,input().split())))
arr = list(map(int,input().split()))
for i in range(n):
    edges.append([0,i+1,arr[i]])
parent = [i for i in range(n+1)]
edges.sort(key=lambda x:x[2])
cnt = 0
answer = 0
for a,b,c in edges:
    if find(a) != find(b):
        union(a,b)
        cnt += 1
        answer += c
        if cnt == n:
            break
print(answer)