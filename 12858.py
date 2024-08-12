import sys
from math import gcd
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def init(s,e,x):
    if s == e:
        seg_tree[x] = arr[s]
        diff_seg_tree[x] = arr[s]-arr[s-1]
        return
    mid = (s+e) >> 1
    init(s,mid,2*x)
    init(mid+1,e,2*x+1)
    seg_tree[x] = gcd(seg_tree[2*x],diff_seg_tree[2*x+1])
    diff_seg_tree[x] = gcd(diff_seg_tree[2*x],diff_seg_tree[2*x+1])

def diff_update(s,e,x,t,v):
    if s == e == t:
        diff_seg_tree[x] += v
        return
    mid = (s+e) >> 1
    if t <= mid:
        diff_update(s,mid,2*x,t,v)
    else:
        diff_update(mid+1,e,2*x+1,t,v)
    diff_seg_tree[x] = gcd(diff_seg_tree[2*x],diff_seg_tree[2*x+1])

def update(s,e,x,l,r,v):
    if e < l or r < s:
        return
    if l <= s and e <= r:
        lazy[x] += v
        return
    mid = (s+e) >> 1
    update(s,mid,2*x,l,r,v)
    update(mid+1,e,2*x+1,l,r,v)

def propagate(s,e,x):
    if lazy[x] != 0:
        if s == e:
            seg_tree[x] += lazy[x]
        else:
            lazy[2*x] += lazy[x]
            lazy[2*x+1] += lazy[x]
        lazy[x] = 0

def left_update(s,e,x,l):
    propagate(s,e,x)
    if s < e:
        mid = (s+e) >> 1
        if l <= mid:
            left_update(s,mid,2*x,l)
        else:
            left_update(mid+1,e,2*x+1,l)
        seg_tree[x] = gcd(seg_tree[2*x],diff_seg_tree[2*x+1])

def search(l,r):
    q = [(1,n,1)]
    _ret = 0
    while q:
        s,e,x = q.pop()
        if e < l or r < s:
            continue
        if l <= s and e <= r:
            if l == s:
                _ret = seg_tree[x]
            else:
                _ret = gcd(_ret,diff_seg_tree[x])
            continue
        mid = (s+e) >> 1
        q.append((mid+1,e,2*x+1))
        q.append((s,mid,2*x))
    return _ret

n = int(input())
arr = [0] + list(map(int,input().split()))

seg_tree = [0]*(4*n)
lazy = [0]*(4*n)
diff_seg_tree = [0]*(4*n)
init(1,n,1)

q = int(input())
for _ in range(q):
    t,a,b = map(int,input().split())
    if t != 0:
        diff_update(1,n,1,a,t)
        if b+1 <= n:
            diff_update(1,n,1,b+1,-t)
        update(1,n,1,a,b,t)
    else:
        left_update(1,n,1,a)
        print(search(a,b))