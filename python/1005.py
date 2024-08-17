def dfs(x):
    global dp
    if dp[x] != -1: return dp[x]
    global weights
    global arr
    _ret = 0
    for i in arr[x]:
        val = dfs(i)
        if _ret < val:
            _ret = val
    dp[x] = weights[x]+_ret
    return dp[x]

t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    weights = list(map(int, input().split()))
    weights.insert(0,0)
    arr = [[] for _ in range(n+1)]
    dp = [-1 for _ in range(n+1)]
    for _ in range(k):
        a,b = map(int, input().split())
        arr[b].append(a)
    w = int(input())
    print(dfs(w))