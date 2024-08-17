import sys
import math
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    numbers = [1 for _ in range(2*n+1)]
    for i in range(2,int(math.sqrt(2*n))+1):
        for j in range((n+1)//i,(2*n)//i+1):
            numbers[j*i] = 0
    print(sum(numbers[n+1:2*n+1]))