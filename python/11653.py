import sys
import math
input = sys.stdin.readline

n = int(input())
for i in range(2,int(math.sqrt(n))+1):
    while n%i == 0:
        print(i)
        n //= i
if n != 1: print(n)