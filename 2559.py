n,k = map(int, input().split())
arr = list(map(int, input().split()))
answer = sum(arr[0:k])
val = answer
for i in range(k,n):
    val = val + arr[i] - arr[i-k]
    if answer < val:
        answer = val
print(answer)