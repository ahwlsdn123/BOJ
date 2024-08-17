import sys
from collections import deque
from math import log2

INF = float('inf')
n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]
depth = [0] * (n + 1)
for _ in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a].append([b, c])
    tree[b].append([a, c])

parent = [[0, 0] for _ in range(n + 1)]
check = [False] * (n + 1)
q = deque([1])
check[1] = True
while q:
    now = q.popleft()
    for b, c in tree[now]:
        if not check[b]:
            q.append(b)
            depth[b] = depth[now] + 1
            check[b] = True
            parent[b][0] = now
            parent[b][1] = c

logN = int(log2(n) + 1)
dp = [[[0, 0, 0] for _ in range(logN)] for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0][0] = parent[i][0]
    dp[i][0][1] = parent[i][1]
    dp[i][0][2] = parent[i][1]

for j in range(1, logN):
    for i in range(1, n + 1):
        dp[i][j][0] = dp[dp[i][j - 1][0]][j - 1][0]
        dp[i][j][1] = min(dp[i][j - 1][1], dp[dp[i][j - 1][0]][j - 1][1])
        dp[i][j][2] = max(dp[i][j - 1][2], dp[dp[i][j - 1][0]][j - 1][2])

k = int(sys.stdin.readline())
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    if depth[a] < depth[b]:
        a, b = b, a
    diff = depth[a] - depth[b]
    shortest = INF
    longest = 0
    for i in range(logN):
        if diff & 1 << i:
            shortest = min(shortest, dp[a][i][1])
            longest = max(longest, dp[a][i][2])
            a = dp[a][i][0]
    if a == b:
        print(shortest, longest)
        continue
    for i in range(logN - 1, -1, -1):
        if dp[a][i][0] != dp[b][i][0]:
            shortest = min(shortest, dp[a][i][1], dp[b][i][1])
            longest = max(longest, dp[a][i][2], dp[b][i][2])
            a = dp[a][i][0]
            b = dp[b][i][0]
    shortest = min(shortest, dp[a][0][1], dp[b][0][1])
    longest = max(longest, dp[a][0][2], dp[b][0][2])
    print(shortest, longest)