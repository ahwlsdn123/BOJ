import sys

mod = 10007

def pow(x,n):
    if n == 1:
        return x
    half = pow(x,n//2)
    return half*half if n%2 == 0 else half*half*x

def div(x,y):
    return x*pow(y,mod-2)%mod

def combination(n,k):
    numor = 1
    denom = 1
    for i in range(k):
        numor *= (n-i)%mod
        denom *= (i+1)%mod
    return div(numor, denom)

def ncard(n):
    result = 0
    for i in range(1, n//4+1): # 가능한 포카드 쌍의 개수 = i
        result += combination(52-i*4,n-i*4)*combination(13,i)*((-1)**(i-1))
        result %= mod
    return result

print(ncard(int(sys.stdin.readline())))