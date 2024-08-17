import sys
from math import log2, log
input = sys.stdin.readline

n,k,q = map(int, input().split())
logN = int(log2(n)+1)
dp = [[0 for _ in range(logN)] for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][0] = (i-2)//k+1
for j in range(1,logN):
    for i in range(1,n+1):
        dp[i][j] = dp[dp[i][j-1]][j-1]
for _ in range(q):
    x,y = map(int, input().split())
    if x > y:
        x,y = y,x
    dx = int(log(((k-1)*(x-1)+1),k))
    dy = int(log(((k-1)*(y-1)+1),k))
    diff = dy-dx
    for i in range(logN):
        if diff & 1<<i:
            y = dp[y][i]
    if x == y:
        print(diff)
        continue
    dist_to_ca = 0
    for i in range(logN-1,-1,-1):
        if dp[x][i] != dp[y][i]:
            x = dp[x][i]
            y = dp[y][i]
            dist_to_ca += 1<<i
    print(2*(dist_to_ca+1)+diff)