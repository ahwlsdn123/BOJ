import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

def dfs(v):
    global visited, ticket, edges
    visited[v] = ticket
    ticket += 1
    for dst in edges[v]:
        if visited[dst] == 0:
            dfs(dst)

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
dfs(r)
for x in visited[1:]:
    print(x)