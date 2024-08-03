def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def lcm(a,b):
    return a // gcd(a,b) * b

d,p,q = map(int, input().split())
if p < q:
    p,q = q,p

ans = float('inf')

for i in range(0, min(d, lcm(p,q))+p,p):
    target = max(d-i,0)
    tmp = target//q*q
    if tmp < target:
        tmp += q
    if ans > tmp+i:
        ans = tmp+i

print(ans)