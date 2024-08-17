import sys
import math
input = sys.stdin.readline

n = int(input())
list = list(map(int, input().split()))
cnt = n
for i in range(n):
    x = list[i]
    if x == 1:
        cnt -= 1
        continue
    for j in range(2,int(math.sqrt(x))+1):
        if x%j == 0:
            cnt -= 1
            break
print(cnt)