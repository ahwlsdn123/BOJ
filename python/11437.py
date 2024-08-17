import sys
from collections import deque
from math import log2

# tree 정보 입력
n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

# bfs 알고리즘으로 각 노드의 부모노드 및 depth 확인
parent = [0] * (n + 1)
depth = [0] * (n + 1)
check = [0] * (n + 1)
q = deque()
q.append(1)
while q:
    now = q.popleft()
    check[now] = 1
    for i in tree[now]:
        if not check[i]:
            q.append(i)
            parent[i] = now
            depth[i] = depth[now] + 1

# sparse table(dp table) 구하기
logN = int(log2(n) + 1)
dp = [[0] * logN for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = parent[i]
for j in range(1, logN):
    for i in range(1, n + 1):
        dp[i][j] = dp[dp[i][j - 1]][j - 1]

# 비교해야 하는 두 노드의 최소 공통 조상 계산
m = int(sys.stdin.readline())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # 깊이 맞추기, 더 깊은 노드 b의 diff 조상을 구하여 깊이를 맞춰줌
    if depth[a] > depth[b]:
        a, b = b, a
    diff = depth[b] - depth[a]
    for i in range(logN):
        if diff & 1 << i:
            b = dp[b][i]
    # 깊이 맞추고, 그 값이 같을 경우 최소 공통 조상은 a
    if a == b:
        print(a)
        continue
    # 루트 노드에서 부터 내려오면서 그 값이 달라지는 순간 찾기
    for i in range(logN - 1, -1, -1):
        if dp[a][i] != dp[b][i]:
            a = dp[a][i]
            b = dp[b][i]
    print(dp[b][0])