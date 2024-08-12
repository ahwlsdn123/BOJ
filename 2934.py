import sys
input = sys.stdin.readline

def propagate(s,e,x):
    if s != e:
        lazy[2*x] += lazy[x]
        lazy[2*x+1] += lazy[x]
    else:
        seg_tree[x] += lazy[x]
    lazy[x] = 0

def update(l,r,v):
    q = [(1,100000,1)]
    while q:
        s,e,x = q.pop()
        propagate(s,e,x)
        if e < l or r < s:
            continue
        if l <= s and e <= r:
            lazy[x] += v
            continue
        mid = (s+e) >> 1
        q.append((s,mid,2*x))
        q.append((mid+1,e,2*x+1))

def search(t):
    s,e,x = 1,100000,1
    while s < e:
        propagate(s,e,x)
        mid = (s+e) >> 1
        if t <= mid:
            e = mid
            x = 2*x
        else:
            s = mid+1
            x = 2*x+1
    propagate(s,e,x)
    _ret = seg_tree[x]
    seg_tree[x] = 0
    return _ret

n = int(input())
seg_tree = [0]*400000
lazy = [0]*400000
for _ in range(n):
    l,r = map(int,input().split())
    print(search(l)+search(r))
    update(l+1,r-1,1)