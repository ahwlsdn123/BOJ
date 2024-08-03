import sys
input = sys.stdin.readline

def find(x,y):
    if parent[x][y] != [x,y]:
        parent[x][y] = find(*parent[x][y])
    return parent[x][y]

def union(x,y):
    visited[x][y] = True
    if x+1 <= m and visited[x+1][y] == True:
        r,c = find(x+1,y)
        parent[r][c] = [x,y]
    if x-1 >= 1 and visited[x-1][y] == True:
        r,c = find(x-1,y)
        parent[r][c] = [x,y]
    if y+1 <= n and visited[x][y+1] == True:
        r,c = find(x,y+1)
        parent[r][c] = [x,y]
    if y-1 >= 1 and visited[x][y-1] == True:
        r,c = find(x,y-1)
        parent[r][c] = [x,y]

m,n,q = map(int,input().split())
num_points = m*n
points = []
mountain = [[0 for _ in range(n+1)]]
for i in range(1,m+1):
    mountain.append([0]+list(map(int,input().split())))
    for j in range(1,n+1):
        points.append([i,j,mountain[-1][j]])
points.sort(key=lambda x:x[2])
query = []
for _ in range(q):
    query.append(list(map(int,input().split())))
low = [0]*q
high = [num_points]*q
ans = [0]*q
fl = True
while fl:
    tmp = [[] for _ in range(num_points)]
    parent = [[[i,j] for j in range(n+1)] for i in range(m+1)]
    visited = [[False for _ in range(n+1)] for _ in range(m+1)]
    fl = False
    for i in range(q):
        if low[i] < high[i]:
            tmp[(low[i]+high[i])//2].append(i)
    for i in range(num_points):
        row = points[i][0]
        col = points[i][1]
        cost = points[i][2]
        union(row,col)
        for j in tmp[i]:
            fl = True
            qx1,qy1,qx2,qy2 = query[j]
            if qx1==qx2 and qy1==qy2:
                high[j] = 0
                ans[j] = mountain[qx1][qy1]
                continue
            x = find(query[j][0],query[j][1])
            y = find(query[j][2],query[j][3])
            if x==y:
                high[j] = i
                ans[j] = cost
            else:
                low[j] = i+1
for i in range(q):
    print(ans[i])