import sys
import math
input = sys.stdin.readline

a,b = map(int, input().split())
c,d = map(int, input().split())

s = a*d+b*c
m = b*d
gcd = math.gcd(s,m)
print(f"{s//gcd} {m//gcd}")