from collections import deque
import sys
input = sys.stdin.readline

def find(w,h):
    global parent
    if parent[w][h] != [w,h]:
        parent[w][h] = find(*parent[w][h])
    return parent[w][h]

def union(w1,h1,w2,h2):
    global parent
    v1 = find(w1,h1)
    v2 = find(w2,h2)
    if parent[v1[0]][v1[1]][0] < parent[v2[0]][v2[1]][0] or (parent[v1[0]][v1[1]][0] == parent[v2[0]][v2[1]][0] and parent[v1[0]][v1[1]][1] < parent[v2[0]][v2[1]][1]):
        parent[v2[0]][v2[1]] = parent[v1[0]][v1[1]]
    else:
        parent[v1[0]][v1[1]] = parent[v2[0]][v2[1]]

def bfs(w,h):
    global arr, parent
    q = deque()
    if h+1 < len(arr[0]) and arr[w][h+1] == 1 and parent[w][h+1] == [w,h+1]:
        q.append([w,h+1])
    if w+1 < len(arr) and arr[w+1][h] == 1 and parent[w+1][h] == [w+1,h]:
        q.append([w+1,h])
    if h-1 >= 0 and arr[w][h-1] == 1 and parent[w][h-1] == [w,h-1]:
        q.append([w,h-1])
    while q:
        i,j = q.popleft()
        parent[i][j] = [w,h]
        if j+1 < len(arr[0]) and arr[i][j+1] == 1 and parent[i][j+1] == [i,j+1]:
            q.append([i,j+1])
        if i+1 < len(arr) and arr[i+1][j] == 1 and parent[i+1][j] == [i+1,j]:
            q.append([i+1,j])
        if j-1 >= 0 and arr[i][j-1] == 1 and parent[i][j-1] == [i,j-1]:
            q.append([i,j-1])

def check_road(h,w):
    global arr,parent,roads
    dist = 1
    while True:
        if h+dist >= len(arr):
            break
        if arr[h+dist][w] == 1:
            if dist >= 3:
                roads.append([[h,w],[h+dist,w],dist-1])
            break
        dist += 1
    dist = 1
    while True:
        if w+dist >= len(arr[0]):
            break
        if arr[h][w+dist] == 1:
            if dist >= 3:
                roads.append([[h,w],[h,w+dist],dist-1])
            break
        dist += 1

n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
parent = [[[i,j] for j in range(m)] for i in range(n)]
num_island = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and parent[i][j] == [i,j]:
            bfs(i,j)
            num_island += 1
roads = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            check_road(i,j)
roads.sort(key=lambda x:x[2])
result = []
for r in roads:
    if find(*r[0]) != find(*r[1]):
        union(*r[0],*r[1])
        result.append(r)
if len(result) == num_island-1:
    answer = 0
    for r in result:
        answer += r[2]
    print(answer)
else:
    print(-1)