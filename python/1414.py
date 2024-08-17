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

n = int(input())
parent = [i for i in range(n)]
edges = []
total = 0
for i in range(n):
    s = input().rstrip()
    for j in range(n):
        if s[j] != '0':
            c = s[j]
            cost = ord(c)-ord('a')+1 if ord('a')<=ord(c)<=ord('z') else ord(c)-ord('A')+27
            total += cost
            if i != j:
                edges.append([i,j,cost])
edges.sort(key=lambda x:x[2])
cnt = 0
answer = 0
tmp = []
for e in edges:
    a,b,c = e
    if find(a) != find(b):
        union(a,b)
        cnt += 1
        answer += c
        tmp.append(e)
if cnt == n-1:
    print(total-answer)
else:
    print(-1)