n = int(input())
arr = list(map(int, input().split()))

arr.sort()
for i in range(1,n):
    arr[i] += arr[i-1]
for i in range(1,n):
    arr[i] += arr[i-1]
print(arr[n-1])