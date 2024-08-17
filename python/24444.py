from collections import deque
import sys
sys.setrecursionlimit(150000)

def bfs(v):
    global visited, ticket, edges
    toVisit = deque()
    toVisit.append(v)
    while toVisit:
        x = toVisit.popleft()
        if visited[x] == 0:
            visited[x] = ticket
            ticket += 1
            toVisit.extend(edges[x])

n,m,r = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
for i in range(n+1):
    edges[i].sort()
visited = [0 for _ in range(n+1)]
ticket = 1
bfs(r)
for x in visited[1:]:
    print(x)