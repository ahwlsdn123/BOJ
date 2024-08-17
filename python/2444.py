import sys
input = sys.stdin.readline

n = int(input())
for i in range(n-1):
    print(" "*(n-i-1), "*"*(2*i+1), sep="")
print("*"*(2*(n-1)+1))
for i in range(n-2, -1, -1):
    print(" "*(n-i-1), "*"*(2*i+1), sep="")