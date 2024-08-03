MOD = 1000000007

def pow(base,exp):
    if exp == 1: return base
    if exp%2 == 0: return (pow(base,exp//2)**2)%MOD
    else: return (pow(base,exp//2)**2*base)%MOD

def combination(n,k):
    _ret = 1
    for i in range(n,n-k,-1):
        _ret *= i
        _ret %= MOD
    div = 1
    for i in range(2,k+1):
        div *= i
        div %= MOD
    div = pow(div,MOD-2)
    _ret *= div
    _ret %= MOD
    return _ret

n,k = map(int, input().split())
k = min(k,n-k)
print(combination(n,k))