import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

def dfs(v):
    global edges, visited, answer
    visited[v] = True
    _ret = 1
    for dst in edges[v]:
        if visited[dst] == False:
            answer[dst] = dfs(dst)
            _ret += answer[dst]
    return _ret

n,r,q = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)
visited = [False for _ in range(n+1)]
answer = [0]*(n+1)
answer[r] = dfs(r)
for _ in range(q):
    print(answer[int(input())])