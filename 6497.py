import sys
input = sys.stdin.readline

def find(v):
    global parent
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v,w):
    global parent
    v = find(v)
    w = find(w)
    if v < w:
        parent[w] = v
    else:
        parent[v] = w

while True:
    m,n = map(int, input().split())
    if m == n == 0: break
    roads = []
    parent = list(range(m))
    answer = 0
    for _ in range(n):
        tmp = list(map(int, input().split()))
        roads.append(tmp)
        answer += tmp[2]
    roads.sort(key=lambda x:x[2])
    for r in roads:
        if find(r[0]) != find(r[1]):
            union(r[0],r[1])
            answer -= r[2]
    print(answer)