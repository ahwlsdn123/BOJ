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
    if u>v:
        parent[u] = v
    else:
        parent[v] = u

while True:
    n,m,k = map(int, input().split())
    if n==0 and m==0 and k==0:
        break
    red_pq = []
    for _ in range(m):
        tmp = input().split()
        a,b = map(int,tmp[1:])
        c = 1 if tmp[0]=='B' else 0
        red_pq.append([a,b,c])
    blue_pq = red_pq.copy()
    red_pq.sort(key=lambda x:x[2])
    blue_pq.sort(key=lambda x:-x[2])
    parent = [i for i in range(n+1)]
    b1 = 0
    for e in red_pq:
        a,b,c = e
        if find(a) != find(b):
            union(a,b)
            b1 += c
    b2 = 0
    parent = [i for i in range(n+1)]
    for e in blue_pq:
        a,b,c = e
        if find(a) != find(b):
            union(a,b)
            b2 += c
    if b1<=k<=b2:
        print(1)
    else:
        print(0)