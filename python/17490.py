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

n,m,k = map(int,input().split())
arr = [0] + list(map(int,input().split()))
edges = []
for i in range(1,n+1):
    edges.append([0,i,arr[i]])
parent = [0,n] + [i for i in range(1,n)]
cnt = n
for _ in range(m):
    a,b = map(int,input().split())
    if a == n or b == n:
        parent[1] = 1
    else:
        if a > b:
            a,b = b,a
        parent[b] = b
    cnt -= 1
if m == 0 or m == 1:
    print('YES')
else:
    edges.sort(key=lambda x:x[2])
    val = 0
    for a,b,c in edges:
        if find(a) != find(b):
            union(a,b)
            cnt += 1
            val += c
            if cnt == n:
                break
    if cnt < n or val > k:
        print('NO')
    else:
        print('YES')