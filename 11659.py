n,m = map(int,input().split())
arr = list(map(int,input().split()))
prefix_sum = [0]
temp = 0
for i in arr:
    temp += i
    prefix_sum.append(temp)
for _ in range(m):
    l,r = map(int, input().split())
    print(prefix_sum[r]-prefix_sum[l-1])