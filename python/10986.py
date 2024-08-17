import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
mods = [0 for _ in range(m)]
mods[arr[0]%m] += 1
val = arr[0]%m
for i in range(1,n):
    val = (arr[i]+val)%m
    mods[val] += 1
answer = mods[0]
for i in range(0,m):
    answer += (mods[i]*(mods[i]-1))//2
print(answer)