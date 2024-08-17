import sys
input = sys.stdin.readline

def init(s,e,x):
    if s == e:
        seg_tree[x] = arr[s]
        return seg_tree[x]
    m = s+e >> 1
    seg_tree[x] = init(s,m,2*x)+init(m+1,e,2*x+1)
    return seg_tree[x]

def lazyUpdate(s,e,x):
    if lazy[x]:
        seg_tree[x] += (e-s+1)*lazy[x]
        if s != e:
            lazy[2*x] += lazy[x]
            lazy[2*x+1] += lazy[x]
        lazy[x] = 0

def update(s,e,x,l,r,diff):
    lazyUpdate(s,e,x)
    if e < l or r < s: return
    if l <= s and e <= r:
        seg_tree[x] += (e-s+1)*diff
        if s != e:
            lazy[2*x] += diff
            lazy[2*x+1] += diff
        return
    m = s+e >> 1
    update(s,m,2*x,l,r,diff)
    update(m+1,e,2*x+1,l,r,diff)
    seg_tree[x] = seg_tree[2*x]+seg_tree[2*x+1]

def out(s,e,x,target):
    lazyUpdate(s,e,x)
    if target < s or e < target: return 0
    if s == e == target: return seg_tree[x]
    m = s+e >> 1
    return out(s,m,2*x,target)+out(m+1,e,2*x+1,target)

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)
seg_tree = [0]*4*n
lazy = [0]*4*n
init(1,n,1)
m = int(input())
for _ in range(m):
    cmd = input().rstrip()
    if cmd[0] == '1':
        _,l,r,diff = map(int,cmd.split())
        update(1,n,1,l,r,diff)
    elif cmd[0] == '2':
        _,target = map(int,cmd.split())
        print(out(1,n,1,target))