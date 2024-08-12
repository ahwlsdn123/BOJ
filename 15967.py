import sys
input = sys.stdin.readline

def init(s,e,x):
    if s == e:
        seg_tree[x] = arr[s]
        return
    mid = (s+e) >> 1
    init(s,mid,2*x)
    init(mid+1,e,2*x+1)
    seg_tree[x] = seg_tree[2*x]+seg_tree[2*x+1]

def propagate(s,e,x):
    if lazy[x] != 0:
        seg_tree[x] += (e-s+1)*lazy[x]
        if s != e:
            lazy[2*x] += lazy[x]
            lazy[2*x+1] += lazy[x]
        lazy[x] = 0

def update(s,e,x,l,r,v):
    propagate(s,e,x)
    if e < l or r < s:
        return
    if l <= s and e <= r:
        seg_tree[x] += (e-s+1)*v
        if s != e:
            lazy[2*x] += v
            lazy[2*x+1] += v
        return
    mid = (s+e) >> 1
    update(s,mid,2*x,l,r,v)
    update(mid+1,e,2*x+1,l,r,v)
    seg_tree[x] = seg_tree[2*x] + seg_tree[2*x+1]

def search(s,e,x,l,r):
    propagate(s,e,x)
    if e < l or r < s:
        return 0
    if l <= s and e <= r:
        return seg_tree[x]
    mid = (s+e) >> 1
    return search(s,mid,2*x,l,r) + search(mid+1,e,2*x+1,l,r)

n,q1,q2 = map(int,input().split())
arr = [0] + list(map(int,input().split()))
seg_tree = [0]*(4*n)
lazy = [0]*(4*n)
init(1,n,1)
for _ in range(q1+q2):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        l,r = cmd[1:]
        print(search(1,n,1,l,r))
    else:
        l,r,v = cmd[1:]
        update(1,n,1,l,r,v)