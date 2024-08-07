import sys
input = sys.stdin.readline

def init(s,e,x):
    if s == e:
        seg_tree[x] = [arr[s],1]
        return
    mid = (s+e)>>1
    init(s,mid,2*x+1)
    init(mid+1,e,2*x+2)
    seg_tree[x][0] = seg_tree[2*x+1][0] ^ seg_tree[2*x+2][0]
    seg_tree[x][1] = seg_tree[2*x+1][1] ^ seg_tree[2*x+2][1]

def propagate(s,e,x):
    if lazy[x] != 0:
        if seg_tree[x][1] == 1:
            seg_tree[x][0] ^= lazy[x]
        if s != e:
            lazy[2*x+1] ^= lazy[x]
            lazy[2*x+2] ^= lazy[x]
        lazy[x] = 0

def update(s,e,x,l,r,c):
    propagate(s,e,x)
    if e < l or r < s:
        return
    if l <= s and e <= r:
        if seg_tree[x][1] == 1:
            seg_tree[x][0] ^= c
        if s != e:
            lazy[2*x+1] ^= c
            lazy[2*x+2] ^= c
        return
    mid = (s+e)>>1
    update(s,mid,2*x+1,l,r,c)
    update(mid+1,e,2*x+2,l,r,c)

def query(s,e,x,a):
    propagate(s,e,x)
    if a < s or e < a:
        return
    if s == e == a:
        print(seg_tree[x][0])
        return
    mid = (s+e)>>1
    query(s,mid,2*x+1,a)
    query(mid+1,e,2*x+2,a)

n = int(input())
arr = list(map(int,input().split()))
seg_tree = [[0,0] for _ in range(4*n)]
lazy = [0]*(4*n)
init(0,n-1,0)
m = int(input())
for _ in range(m):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        a,b,c = cmd[1:]
        update(0,n-1,0,a,b,c)
    else:
        a = cmd[1]
        query(0,n-1,0,a)