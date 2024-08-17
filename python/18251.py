import sys;

input = sys.stdin.readline

N = int(input().strip())
weight = list(map(int, input().split()))
nodes = []

for idx in range(N):
    if idx + 1 == 1 << len(nodes):
        nodes.append([])
    nodes[-1].append(idx)


def inorder(idx, y, limit):
    global s, ans

    if idx * 2 + 1 <= N and y < limit:
        inorder(idx * 2 + 1, y + 1, limit)

    if s + weight[idx] < 0:
        ans = max(ans, weight[idx])
        s = 0
    else:
        s += weight[idx]
        ans = max(ans, s)

    if idx * 2 + 2 <= N and y < limit:
        inorder(idx * 2 + 2, y + 1, limit)


ans = float('-inf')
for i in range(len(nodes)):
    for j in range(i, len(nodes)):
        s = 0
        for idx in nodes[i]:
            inorder(idx, i, j)

print(ans)