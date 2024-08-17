import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

def dfs(v):
    global weights, edges, visited
    visited[v] = True
    a1 = weights[v]
    a2 = 0
    for dst in edges[v]:
        if not visited[dst]:
            a,b = dfs(dst)
            a1 += b
            a2 += max(a,b) # 적어도 한 번은 a를 더해야 함.
    return a1, a2

n = int(input())
weights = list(map(int, input().split()))
weights.insert(0,0)
edges = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
print(max(dfs(1)))