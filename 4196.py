import sys
sys.setrecursionlimit(10 ** 6)


def dfs(node, visited, stack):
    visited[node] = 1
    for ne in graph[node]:
        if visited[ne] == 0:
            dfs(ne, visited, stack)
    stack.append(node)


def reverse_dfs(node, visited, scc):
    global idid
    visited[node] = 1
    ids[node] = idid
    scc.append(node)
    for ne in reverse_graph[node]:
        if visited[ne] == 0:
            reverse_dfs(ne, visited, scc)


t = int(sys.stdin.readline())
for _ in range(t):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v + 1)]
    reverse_graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        reverse_graph[b].append(a)
    stack = []
    visited = [0] * (v + 1)
    for i in range(1, v + 1):
        if visited[i] == 0:
            dfs(i, visited, stack)
    idid = 0
    ids = [-1] * (v + 1)
    visited = [0] * (v + 1)
    result = []
    while stack:
        ssc = []
        node = stack.pop()
        if visited[node] == 0:
            idid += 1
            reverse_dfs(node, visited, ssc)
            result.append(sorted(ssc))
    scc_indegree = [0] * (idid + 1)
    for i in range(1, v + 1):
        for to in graph[i]:
            if ids[i] != ids[to]:
                scc_indegree[ids[to]] += 1
    cnt = 0
    for i in range(1, len(scc_indegree)):
        if scc_indegree[i] == 0:
            cnt += 1
    print(cnt)