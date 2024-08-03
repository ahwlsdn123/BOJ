import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())
v -= (a+1)
a -= b
print(v//a+2)