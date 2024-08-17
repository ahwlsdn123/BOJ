import sys, heapq
input = sys.stdin.readline

n,m = map(int, input().split())
in_degree = [0]*(n+1)
edges = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    in_degree[b] += 1
    edges[a].append(b)

queue = []
for i in range(1,n+1):
    if in_degree[i] == 0:
        heapq.heappush(queue, i)
answer = []
while queue:
    x = heapq.heappop(queue)
    answer.append(x)
    for e in edges[x]:
        in_degree[e] -= 1
        if in_degree[e] == 0:
            heapq.heappush(queue, e)

print(*answer)