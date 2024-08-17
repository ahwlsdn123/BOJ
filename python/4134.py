import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 0 or n == 1 or n == 2:
        print(2)
        continue
    while True:
        b = True
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0:
                b = False
                break
        if b:
            break
        n += 1
    print(n)