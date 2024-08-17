import sys
input = sys.stdin.readline
 
MAX = 100001
 
def find(x):
    if x == p[x]: return x
    p[x] = find(p[x])
    return p[x]
 
def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        p[x] = y
        cnt[y] += cnt[x]
 
n,m = map(int, input().split())
g = []
for i in range(m):
    start,end,cost = map(int, input().split())
    g.append([cost, start, end])
 
g.sort(key=lambda x:x[0])
 
q = int(input())
query = []
for i in range(q):
    start, end = map(int, input().split())
    query.append([start, end])
 
lo = [0 for _ in range(MAX)]
hi = [m+1 for _ in range(MAX)]
ans = [[0,0] for _ in range(MAX)]
fl = True
while fl:
    # print(lo[:2],hi[:2])
    a = [[] for _ in range(MAX)]
    p = [i for i in range(MAX)]
    cnt = [1 for i in range(MAX)]
    fl = False
    for i in range(q):
        if lo[i]<hi[i]:
            a[(lo[i]+hi[i])//2].append(i)
 
    for i in range(1, m+1):
        cost = g[i-1][0]
        start = g[i-1][1]
        end = g[i-1][2]
        union(start, end)
 
        for j in a[i]:
            fl = True
            x = find(query[j][0])
            y = find(query[j][1])
            if x==y:
                hi[j] = i
                ans[j][0] = cost
                ans[j][1] = cnt[find(x)]
            else:
                lo[j] = i+1
 
for i in range(q):
    if lo[i] == m+1: print(-1)
    else: print(ans[i][0], ans[i][1])