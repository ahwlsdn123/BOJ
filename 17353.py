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
    if lazy[x] != [0,0]:
        seg_tree[x] += lazy[x][0]*(e-s+1) + lazy[x][1]*((e-s)*(e-s+1)//2)
        if s != e:
            lazy[2*x][0] += lazy[x][0]
            lazy[2*x][1] += lazy[x][1]
            lazy[2*x+1][0] += lazy[x][0] + ((e-s)//2 + 1)*lazy[x][1]
            lazy[2*x+1][1] += lazy[x][1]
        lazy[x] = [0,0]

def update(s,e,x,l,r,v):
    propagate(s,e,x)

    if e < l or r < s:
        return
    
    if l <= s and e <= r:
        seg_tree[x] += v*(e-s+1) + (s+e-2*l)*(e-s+1)//2
        if s != e:
            lazy[2*x][0] += v + (s-l)
            lazy[2*x][1] += 1
            lazy[2*x+1][0] += v + (s+e)//2 - l + 1
            lazy[2*x+1][1] += 1
        return
    
    mid = (s+e) >> 1
    update(s,mid,2*x,l,r,v)
    update(mid+1,e,2*x+1,l,r,v)
    seg_tree[x] = seg_tree[2*x]+seg_tree[2*x+1]

def query(s,e,x,t):
    propagate(s,e,x)

    if t < s or e < t:
        return 0
    
    if s == e == t:
        return seg_tree[x]
    
    mid = (s+e) >> 1
    return query(s,mid,2*x,t) + query(mid+1,e,2*x+1,t)

n = int(input())
arr = [0] + list(map(int,input().split()))
seg_tree = [0]*(4*n)
lazy = [[0,0] for _ in range(4*n)]
init(1,n,1)
q = int(input())
for _ in range(q):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        _,l,r = cmd
        update(1,n,1,l,r,1)
    else:
        _,x = cmd
        print(query(1,n,1,x))