import sys
input = sys.stdin.readline

def get_dist(c1,c2):
    return ((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)**0.5

def find(x):
    global parent
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    global parent
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int, input().split())
coords = [[0,0]]
parent = list(range(n+1))
for _ in range(n):
    coords.append(list(map(int, input().split())))

for _ in range(m):
    a,b = map(int, input().split())
    union(a,b)

possible = []
for i in range(1, len(coords)-1):
    for j in range(i+1, len(coords)):
        possible.append([get_dist(coords[i],coords[j]),i,j])
possible.sort()
answer = 0
for p in possible:
    cost, p1, p2 = p[0], p[1], p[2]
    if find(p1) != find(p2):
        union(p1,p2)
        answer += cost
print("{:.2f}".format(answer))