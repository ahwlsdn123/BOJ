import sys
input = sys.stdin.readline

def init(s,e,x):
    global seg_tree
    if s == e:
        seg_tree[x] = [arr[s],1]
        return
    mid = (s+e) >> 1
    init(s,mid,2*x+1)
    init(mid+1,e,2*x+2)
    seg_tree[x][0] = seg_tree[2*x+1][0] ^ seg_tree[2*x+2][0]
    seg_tree[x][1] = (seg_tree[2*x+1][1] + seg_tree[2*x+2][1]) % 2

def propagate(s,e,x):
    if lazy[x] != 0:
        if seg_tree[x][1] == 1:
            seg_tree[x][0] ^= lazy[x]
        if s != e:
            lazy[2*x+1] ^= lazy[x]
            lazy[2*x+2] ^= lazy[x]
        lazy[x] = 0

def update(s,e,x,l,r,k):
    propagate(s,e,x)

    if r < s or e < l:
        return
    
    if l <= s and e <= r:
        if seg_tree[x][1] == 1:
            seg_tree[x][0] ^= k
        if s != e:
            lazy[2*x+1] ^= k
            lazy[2*x+2] ^= k
        return
    
    mid = (s+e) >> 1
    update(s,mid,2*x+1,l,r,k)
    update(mid+1,e,2*x+2,l,r,k)
    seg_tree[x][0] = seg_tree[2*x+1][0] ^ seg_tree[2*x+2][0]

def query(s,e,x,l,r):
    propagate(s,e,x)
    
    if e < l or r < s:
        return 0
    
    if l <= s and e <= r:
        return seg_tree[x][0]
    
    mid = (s+e) >> 1
    return query(s,mid,2*x+1,l,r) ^ query(mid+1,e,2*x+2,l,r)

n = int(input())
arr = list(map(int,input().split()))
seg_tree = [[0,0] for _ in range(4*n)]
lazy = [0]*(4*n)
init(0,n-1,0)
m = int(input())
for _ in range(m):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        _,l,r,k = cmd
        update(0,n-1,0,l,r,k)
    else:
        _,l,r = cmd
        print(query(0,n-1,0,l,r))