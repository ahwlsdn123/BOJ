import sys
input = sys.stdin.readline

def dfs(v):
    global weights, edges, visited
    visited[v] = True
    a1 = weights[v]
    a2 = 0
    s1 = set([v])
    s2 = set()
    for dst in edges[v]:
        if not visited[dst]:
            a,b,c,d = dfs(dst)
            a1 += b
            s1.update(d)
            if a > b:
                a2 += a
                s2.update(c)
            else:
                a2 += b
                s2.update(d)
    return a1, a2, s1, s2

n = int(input())
weights = list(map(int, input().split()))
weights.insert(0,0)
edges = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
p1,p2,q1,q2 = dfs(1)
if p1>p2:
    print(p1)
    for q in q1:
        print(q, end=" ")
    print()
else:
    print(p2)
    for q in q2:
        print(q, end=" ")
    print()