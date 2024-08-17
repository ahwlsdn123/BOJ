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

t = int(input())
for _ in range(t):
    r,c = map(int,input().split())
    parent = [i for i in range(r*c)]
    edges = []
    for i in range(r):
        tmp = list(map(int,input().split()))
        for j in range(c-1):
            edges.append([c*i+j,c*i+j+1,tmp[j]])
    for i in range(r-1):
        tmp = list(map(int,input().split()))
        for j in range(c):
            edges.append([c*i+j,c*(i+1)+j,tmp[j]])
    edges.sort(key=lambda x:x[2])
    cnt = 0
    answer = 0
    for a,b,cost in edges:
        if find(a) != find(b):
            union(a,b)
            cnt += 1
            answer += cost
            if cnt == r*c-1:
                print(answer)
                break