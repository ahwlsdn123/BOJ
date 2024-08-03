import sys
import math
input = sys.stdin.readline

n = int(input())
list = []
for _ in range(n):
    list.append(int(input()))
sub_list = []
for i in range(n-1):
    sub_list.append(list[i+1]-list[i])
gcd = sub_list[0]
for i in range(n-1):
    gcd = math.gcd(gcd,sub_list[i])
answer = 0
for i in range(n-1):
    answer += sub_list[i]//gcd-1
print(answer)