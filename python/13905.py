import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
S, E = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N+1)]
answer = 0

for _ in range(M):
    h1, h2, k = map(int, sys.stdin.readline().split())
    edges[h1].append((h2, k))
    edges[h2].append((h1, k))


left = 1
right = 10 ** 6

while left <= right:
    mid = (left + right) // 2
    flag = False
    # BFS
    visit = [False] * (N+1)
    q = deque()
    q.append(S)
    visit[S] = True
    while q:
        now = q.popleft()
        if now == E:
            flag = True
            break
        for node, weight in edges[now]:
            if not visit[node] and weight >= mid:
                q.append(node)
                visit[node] = True

    if flag:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)