import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
arr = [[0 for _ in range(m+1)]]
for i in range(n):
    s = input().rstrip()
    tmp = [0]
    for j in range(m):
        if (i+j)%2 != 0:
            tmp.append(int(s[j]=='B'))
        else:
            tmp.append(int(s[j]=='W'))
        tmp[j+1] += tmp[j]
    arr.append([x+y for x,y in zip(arr[i],tmp)])
min_val = 40000000
max_val = 0
for i in range(n-k+1):
    for j in range(m-k+1):
        val = arr[i+k][j+k] - arr[i+k][j] - arr[i][j+k] + arr[i][j]
        min_val = min(min_val,val)
        max_val = max(max_val,val)
print(min(min_val,k*k-max_val))