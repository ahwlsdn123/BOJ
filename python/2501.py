import sys
input = sys.stdin.readline

n, k = map(int, input().split())
b = True
for i in range(1,n+1):
    if n%i==0:
        k -= 1
        if k == 0:
            print(i)
            b = False
            break
if b: print(0)