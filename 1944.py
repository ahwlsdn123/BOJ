import sys
from collections import deque
input = sys.stdin.readline

def BFS(s0,s1,e0,e1):
    global maze
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append([s0,s1,0])
    visited[s0][s1] = True
    while q:
        p0,p1,depth = q.popleft()
        if p0 == e0 and p1 == e1:
            return depth
        if p0+1<n and maze[p0+1][p1] != '1' and not visited[p0+1][p1]:
            visited[p0+1][p1] = True
            q.append([p0+1,p1,depth+1])
        if p0-1>=0 and maze[p0-1][p1] != '1' and not visited[p0-1][p1]:
            visited[p0-1][p1] = True
            q.append([p0-1,p1,depth+1])
        if p1+1<n and maze[p0][p1+1] != '1' and not visited[p0][p1+1]:
            visited[p0][p1+1] = True
            q.append([p0,p1+1,depth+1])
        if p1-1>=0 and maze[p0][p1-1] != '1' and not visited[p0][p1-1]:
            visited[p0][p1-1] = True
            q.append([p0,p1-1,depth+1])
    return -1

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

n,m = map(int, input().split())
maze = []
keys = []
for i in range(n):
    s = input().rstrip()
    maze.append(s)
    for j in range(n):
        if s[j] == 'S' or s[j] == 'K':
            keys.append([i,j])
edges = []
failed = False
for i in range(m+1):
    for j in range(i+1,m+1):
        s0,s1 = keys[i]
        e0,e1 = keys[j]
        d = BFS(s0,s1,e0,e1)
        if d == -1: 
            failed = True
            break
        edges.append([i,j,d])
    if failed:
        break
if failed:
    print(-1)
else:
    parent = [i for i in range(m+1)]
    edges.sort(key=lambda x:x[2])
    answer = 0
    for i0,i1,d in edges:
        if find(i0) != find(i1):
            union(i0,i1)
            answer += d
    print(answer)