n = int(input())
dp = [[0 for _ in range(101)] for _ in range(101)] # answer = dp[1][100]
l = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(n):
    a,b = map(int, input().split())
    if a>b:
        a,b = b,a
    l[a][b] += 1
for k in range(1,100):
    for i in range(1,101-k):
        j = i+k
        elements = [dp[i][t]+dp[t][j] for t in range(i+1,j)]
        elements.append(0)
        dp[i][j] = max(elements) + l[i][j]
print(dp[1][100])