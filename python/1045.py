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
roads = []
for i in range(n):
    s = input().rstrip()
    for j in range(i+1,n):
        if s[j] == 'Y':
            roads.append([i,j])
parent = [i for i in range(n)]
cnt = 0
answer = [0]*n
trash = []
for i in range(len(roads)):
    u,v = roads[i]
    if find(u) != find(v):
        union(u,v)
        cnt += 1
        answer[u] += 1
        answer[v] += 1
        if cnt == n-1:
            trash.extend(roads[i+1:])
            break
    else:
        trash.append([u,v])
if cnt < n-1 or m < cnt:
    print(-1)
else:
    try:
        for i in range(m-cnt):
            u,v = trash[i]
            answer[u] += 1
            answer[v] += 1
        print(*answer)
    except:
        print(-1)