import sys
input = sys.stdin.readline
MOD = 1000000007

def init(s,e,x):
    if s == e:
        seg_tree[x] = arr[s]
        return
    mid = (s+e) >> 1
    init(s,mid,2*x)
    init(mid+1,e,2*x+1)
    seg_tree[x] = (seg_tree[2*x]+seg_tree[2*x+1]) % MOD

def propagate(s,e,x):
    if lazy[x] != [1,0]:
        seg_tree[x] = (lazy[x][0]*seg_tree[x] + lazy[x][1]*(e-s+1)) % MOD
        if s != e:
            lazy[2*x][0] = (lazy[x][0]*lazy[2*x][0]) % MOD
            lazy[2*x][1] = (lazy[x][0]*lazy[2*x][1]+lazy[x][1]) % MOD
            lazy[2*x+1][0] = (lazy[x][0]*lazy[2*x+1][0]) % MOD
            lazy[2*x+1][1] = (lazy[x][0]*lazy[2*x+1][1]+lazy[x][1]) % MOD
        lazy[x] = [1,0]

def update(s,e,x,l,r,q,v):
    propagate(s,e,x)
    if e < l or r < s:
        return
    if l <= s and e <= r:
        if q == 1:
            seg_tree[x] += v*(e-s+1)
            seg_tree[x] %= MOD
        elif q == 2:
            seg_tree[x] *= v
            seg_tree[x] %= MOD
        elif q == 3:
            seg_tree[x] = (v*(e-s+1)) % MOD
        if s != e:
            if q == 1:
                lazy[2*x][1] += v
                lazy[2*x][1] %= MOD
                lazy[2*x+1][1] += v
                lazy[2*x+1][1] %= MOD
            elif q == 2:
                lazy[2*x][0] *= v
                lazy[2*x][0] %= MOD
                lazy[2*x][1] *= v
                lazy[2*x][1] %= MOD
                lazy[2*x+1][0] *= v
                lazy[2*x+1][0] %= MOD
                lazy[2*x+1][1] *= v
                lazy[2*x+1][1] %= MOD
            elif q == 3:
                lazy[2*x] = [0,v]
                lazy[2*x+1] = [0,v]
        return
    mid = (s+e) >> 1
    update(s,mid,2*x,l,r,q,v)
    update(mid+1,e,2*x+1,l,r,q,v)
    seg_tree[x] = (seg_tree[2*x]+seg_tree[2*x+1]) % MOD

def query(s,e,x,l,r):
    propagate(s,e,x)
    if e < l or r < s:
        return 0
    if l <= s and e <= r:
        return seg_tree[x]
    mid = (s+e) >> 1
    return (query(s,mid,2*x,l,r) + query(mid+1,e,2*x+1,l,r)) % MOD

n = int(input())
arr = [0] + list(map(int,input().split()))
seg_tree = [0]*(4*n)
lazy = [[1,0] for _ in range(4*n)]
init(1,n,1)
m = int(input())
for _ in range(m):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1 or cmd[0] == 2 or cmd[0] == 3:
        q,x,y,v = cmd
        update(1,n,1,x,y,q,v)
    else:
        x,y = cmd[1:]
        print(query(1,n,1,x,y))