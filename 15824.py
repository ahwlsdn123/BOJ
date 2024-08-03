# https://www.acmicpc.net/problem/15824

import sys
MOD = 1000000007

def pow(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a
    half = pow(a,b//2)
    return half*half%MOD if b%2 == 0 else half*half*a%MOD

n = int(sys.stdin.readline().strip())
scovilles = sorted(list(map(int, sys.stdin.readline().strip().split())))
answer = 0

for i in range(n):
    answer += scovilles[i] * (pow(2,i) - pow(2,n-1-i))

print(answer % MOD)