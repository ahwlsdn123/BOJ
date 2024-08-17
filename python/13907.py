import sys, heapq

# 입력부
vertex, edges, taxes = map(int, sys.stdin.readline().split())
start, end = map(int, sys.stdin.readline().split())

# adj : 인접 리스트, INF : 무한대, d : 2차원 다익스트라 배열
adj = [[] for _ in range(vertex)]
INF = 10000000000000000000
tax_rate = []
d = [[INF] * vertex for _ in range(vertex)]

# 최소값을 찾는 것이므로 ans를 무한대 값으로 초기화
ans = INF

# dijsta : 2차원 배열 d를 갱신시키는 함수
def dijstra(v):
    global ans
    d[v][0] = 0
    min_q = []
    min_q.append((d[v][0], v, 0))
    while len(min_q) != 0:
        distance = min_q[0][0]
        current = min_q[0][1]
        visited = min_q[0][2]
        heapq.heappop(min_q)
        flag = False
        # 불필요한 경우 1:
        # 이미 최소 거리가 있다면 굳이 정점을 더 거쳐가지 않아도 되므로
        # flag를 True로 바꿔준다
        for i in range(visited):
            if d[current][i] < distance:
                flag = True
                break
        # 불필요한 경우 2:
        # 불필요한 경우 1에서 걸려진 경우거나, 똑같이 j번째 정점을 방문해도
        # 거리가 더 작은 쪽이 유지되어야 하므로
        # 현재 거리가 배열에 저장된 거리보다 크다면 굳이 갱신이 일어나지 않는다
        if flag or d[current][visited] < distance:
            continue
        # 불필요한 경우 3:
        # 애초에 현재 정점이 도착정점이라면 굳이 다른 정점을 탐색하지 않아도 된다
        if current == end - 1:
            ans = min(ans, d[current][visited])
            continue
        for i in range(len(adj[current])):
            next = adj[current][i][0]
            nextdistance = adj[current][i][1] + distance
            # 배열 d의 범위를 벗어나지 않고 거리가 더 작다면 갱신
            if visited + 1 < vertex and nextdistance < d[next][visited + 1]:
                d[next][visited + 1] = nextdistance
                heapq.heappush(min_q, (nextdistance, next, visited + 1))

# 인접리스트 생성
for i in range(edges):
    a, b, w = map(int, sys.stdin.readline().split())
    adj[a - 1].append([b - 1, w])
    adj[b - 1].append([a - 1, w])

# 세금 입력
for i in range(taxes):
    tax_rate.append(int(sys.stdin.readline()))

# 다익스트라 실행
dijstra(start - 1)

# 세금이 부과되지 않은 경우 정답 출력
print(ans)

# 도착 정점에 대한 경우만 세금률에 따라 갱신
for i in tax_rate:
    for j in range(vertex):
        if d[end - 1][j] != INF:
            d[end - 1][j] = d[end - 1][j] + i * j
    # 각 세금률에 따른 정답 출력
    print(min(d[end - 1]))