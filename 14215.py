import sys
input = sys.stdin.readline

list = list(map(int, input().split()))
max = max(list)
list.remove(max)
sum = list[0]+list[1]
if sum <= max:
    print(2*sum-1)
else:
    print(sum+max)